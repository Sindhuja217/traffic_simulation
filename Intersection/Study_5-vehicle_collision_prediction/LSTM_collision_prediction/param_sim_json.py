import random
import os
import sumolib
import traci
import xml.etree.ElementTree as ET
import re
import csv
import json
import pandas as pd


# Define the SUMO command
sumoCmd = [sumolib.checkBinary('sumo'), '-c', 'intersec.sumocfg', '--log', 'simulation_main.log','--random']

collision_file = os.path.join('output', 'collisions.xml')

def simulation_sumo_intersec():
    numbs = random.randint(0, 5)
    xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- VTypes -->
    <vType id="non-ego" guiShape="passenger" carFollowModel="EIDM" color="blue" tau="1.5" minGap="2.5" accel="2.6" decel="4.5" sigmaerror="0.1" maxSpeed="27.78" emergencyDecel="4.5" />
    <vType id="ego" guiShape="passenger" carFollowModel="EIDM" color="red" tau="0.1" minGap="1.0" accel="6.0" decel="10.0" sigmaerror="0.5" maxSpeed="41.67" emergencyDecel="11.0" jmDriveRedSpeed="10.0" jmDriveAfterRedTime="4.0" jmDriveAfterYellowTime="4.0"/>        
    <!-- Routes -->
    <routeDistribution id="rd1">
        <route id="r_0" edges="-E6 -E5 -E1 E3 E7" probability="0.2"/>
        <route id="r_1" edges="E0 E1 E5 E6" probability="0.2"/>
        <route id="r_2" edges="E2 E3 E7" probability="0.2"/>
        <route id="r_3" edges="-E7 -E3 -E0" probability="0.2"/>
        <route id="r_4" edges="-E6 -E5 -E1 -E0" probability="0.2"/>
    </routeDistribution>
    <flow id="non_ego_flow" type='non-ego' route='rd1' begin="0" end="20" number="10">
    </flow>
    <vehicle id="ego_vehicle" type='ego' depart="{numbs}" route="rd1"/>
</routes>
"""
    with open("intersec.rou.xml", "w") as xml_file:
        xml_file.write(xml_template)

    traci.start(sumoCmd)

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

    traci.close()
    collision_detected = False
    if os.path.exists(collision_file):
        collision_tree = ET.parse(collision_file)
        collision_root = collision_tree.getroot()
        if collision_root.find('collision') is not None:
            collision_detected = True
    
    if collision_detected == True:
        fcd_data = get_fcd_collision_data()
    else:
        fcd_data = get_fcd_non_collision_data()
    return fcd_data

def get_fcd_non_collision_data():
    fcd_tree = ET.parse('output/fcd_op.xml')
    fcd_root = fcd_tree.getroot()
    fcd_ls = []
    for timestep in fcd_root:
        time = float(timestep.attrib['time'])
        for vehicle in timestep:
            vehicle_data = {'time': time}
            vehicle_data.update(vehicle.attrib)
            fcd_ls.append(vehicle_data)
    fcd_data = pd.DataFrame(fcd_ls)
    numeric_cols = ['time', 'x', 'y', 'angle', 'speed', 'pos', 'slope', 'acceleration', 'distance']
    fcd_data[numeric_cols] = fcd_data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    fcd_data['collision_occurred'] = 0
    fcd_data['lane'] = fcd_data['lane'].str.replace(':', '').str.replace('=', '')
    return fcd_data

def get_fcd_collision_data():
    collision_tree = ET.parse(collision_file)
    collisions_root = collision_tree.getroot()
    fcd_tree = ET.parse('output/fcd_op.xml')
    fcd_root = fcd_tree.getroot()
    
    fcd_ls = []
    collisions_ls = []

    for timestep in fcd_root:
        time = timestep.attrib['time']
        for vehicle in timestep:
            vehicle_data = {'time': time}
            vehicle_data.update(vehicle.attrib)
            fcd_ls.append(vehicle_data)

    for collision in collisions_root:
        collision_dt = collision.attrib
        collisions_ls.append(collision_dt)

    fcd_data = pd.DataFrame(fcd_ls)
    collision_data = pd.DataFrame(collisions_ls)
    collision_data['collider_marker'] = 1
    collision_data['victim_marker'] = 1

    collider_merge = pd.merge(fcd_data, collision_data, left_on=['time', 'id', 'type', 'speed'], 
                            right_on=['time', 'collider', 'colliderType', 'colliderSpeed'], how='left')

    victim_merge = pd.merge(fcd_data, collision_data, left_on=['time', 'id', 'type', 'speed'], 
                            right_on=['time', 'victim', 'victimType', 'victimSpeed'], how='left')

    collider_merge['collision_occurred'] = collider_merge['collider_marker'].notnull()
    victim_merge['collision_occurred'] = victim_merge['victim_marker'].notnull()

    fcd_data['collision_occurred'] = (collider_merge['collision_occurred'] | victim_merge['collision_occurred']).astype(int)
    fcd_data['lane'] = fcd_data['lane'].str.replace(':', '').str.replace('=', '')
    numeric_cols = ['time', 'x', 'y', 'angle', 'speed', 'pos', 'slope', 'acceleration', 'distance']
    fcd_data[numeric_cols] = fcd_data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    return fcd_data     

def dataset_transformer(dataset):
    ego_data = dataset[dataset['id'] == "ego_vehicle"]
    #ego_data = ego_df[ego_df['time'] <= round(float(ego_df[ego_df['collision_occurred'] == 1]['time']) + 0.5, 1)]
    ego_vehicle_id = 'ego_vehicle'
    non_ego_data = dataset[dataset['id'] != ego_vehicle_id]
    non_ego_vehicle_ids = non_ego_data['id'].unique()

    transformed_data = []

    for time in ego_data['time'].unique():
        ego_vehicle_data = ego_data[ego_data['time'] == time]

        time_frame_data = {
            'time': time,
            'ego_id': ego_vehicle_id,
            'ego_speed': ego_vehicle_data['speed'].values[0],
            'ego_acceleration': ego_vehicle_data['acceleration'].values[0],
            'ego_x': ego_vehicle_data['x'].values[0],
            'ego_y': ego_vehicle_data['y'].values[0]
        }

        min_displacement = float('inf')
        closest_vehicle = None

        for non_ego_id in non_ego_vehicle_ids:
            non_ego_vehicle_data = non_ego_data[(non_ego_data['id'] == non_ego_id) & (non_ego_data['time'] == time)]

            if not non_ego_vehicle_data.empty:
                relative_displacement = ((non_ego_vehicle_data['x'].values[0] - time_frame_data['ego_x'])**2 + 
                                         (non_ego_vehicle_data['y'].values[0] - time_frame_data['ego_y'])**2)**0.5
                if relative_displacement < min_displacement:
                    min_displacement = relative_displacement
                    closest_vehicle = non_ego_id
                    time_frame_data['nearest_vehicle_id'] = non_ego_id
                    time_frame_data['nearest_vehicle_speed'] = non_ego_vehicle_data['speed'].values[0]
                    time_frame_data['nearest_vehicle_acceleration'] = non_ego_vehicle_data['acceleration'].values[0]
                    time_frame_data['nearest_vehicle_relative_displacement'] = relative_displacement

        if closest_vehicle is None:
            time_frame_data['nearest_vehicle_id'] = 'none'
            time_frame_data['nearest_vehicle_relative_speed'] = 0
            time_frame_data['nearest_vehicle_acceleration'] = 0
            time_frame_data['nearest_vehicle_displacement'] = 0

        time_frame_data['collision_occurred'] = ego_vehicle_data['collision_occurred'].values[0]

        transformed_data.append(time_frame_data)

    transformed_df = pd.DataFrame(transformed_data)
    return transformed_df


def run_simulations_only_collisions():
    no_collision_count = 0
    collision_count = 0
    while no_collision_count < 5:
        fcd_data = simulation_sumo_intersec()
        if fcd_data['collision_occurred'].sum() == 0:
            no_collision_count += 1
            ego_df = dataset_transformer(fcd_data)
            csv_filename = f"datasets/simulation_no_collision_{no_collision_count}_dataset.csv"
            ego_df.to_csv(csv_filename, index=False)

    while collision_count < 5:
        fcd_data_col = simulation_sumo_intersec()
        if fcd_data_col['collision_occurred'].sum() > 0:
            collision_count += 1
            ego_df = dataset_transformer(fcd_data_col)
            csv_filename = f"datasets/simulation_collision_{collision_count}_dataset.csv"
            ego_df.to_csv(csv_filename, index=False)
            fcd_data_col.to_csv(f'datasets/collision{collision_count}.csv', index=False)

    return collision_count 

col_num = run_simulations_only_collisions()
print(col_num)

