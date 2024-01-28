import os
import sumolib
import traci
import xml.etree.ElementTree as ET
import re
import matplotlib.pyplot as plt
import numpy as np

parameter_name = os.environ.get("parameter_name", "jmIgnoreFoeProb")
param_val = os.environ.get("param_val", [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]) 
param_val = param_val.strip('][').split(',')
param_val = [float(x) for x in param_val]

print(f"param_name {parameter_name} --- param_val {param_val}")

# SUMO command - make sure to have sumo installed and in your path variable (environment variables)
sumoCmd = [sumolib.checkBinary('sumo'), '-c', 'intersec_1.sumocfg', '--log', 'simulation_main.log','--random']

# commands to run on terminal
# export parameter_name="emergencyDecel" && export param_val="[5,6,7,8,9,10,15,30,50,60]" && python sim.py
# export parameter_name="tau" && export param_val="[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]" && python sim.py
# export parameter_name="decel" && export param_val="[0.5,1,2,3,4,5,6,7,8]" && python sim.py
# export parameter_name="accel" && export param_val="[0.5,1,2,3,4,5,7,9,10,20,50]" && python sim.py
# export parameter_name="impatience" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python sim.py
# export parameter_name="jmIgnoreFoeProb" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python sim.py
# export parameter_name="jmSigmaMinor" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python sim.py
# export parameter_name="sigmaerror" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python sim.py
# export parameter_name="jerkmax" && export param_val="[0.5,1,2,3,4,5,6,7,8,9,10]" && python sim.py
# export parameter_name="tpreview" && export param_val="[0.01,0.02]" && python sim.py

collision_counts = {}
brakes_counts = {}
x_counts = {}
cols = []

for value in param_val:
    tree = ET.parse('intersec_1.rou.xml')
    root = tree.getroot()

    vtype = root.find("./vType[@id='ego_veh']")

    vtype.set(parameter_name, str(value))

    tree.write('intersec_1.rou.xml')

    traci.start(sumoCmd)

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

    traci.close()
    # using simulation_main.log to get the number of emergency brakes
    with open('simulation_main.log', 'r') as log_file:
        log_content = log_file.read()
        brakes_matches = re.findall(r"Warning:.*emergency braking", log_content, re.MULTILINE)

    brakes_count = len(brakes_matches)

    brakes_counts[value] = brakes_count

    data_folder = 'output'
    collision_file = os.path.join(data_folder, 'collisions.xml')
    
    # using collisions.xml to get the number of collisions
    if os.path.exists(collision_file):
        collision_tree = ET.parse(collision_file)
        collision_root = collision_tree.getroot()
        
        collider_speeds = []
        victim_speeds = []
        lane = []
        pos = []
        colider = []
        victim = []
        time = []
        for collision in collision_root.findall('collision'):
            coll_lane = collision.get('lane')
            coll_time = float(collision.get('time'))
            coll_pos = float(collision.get('pos'))
            coll_colider = collision.get('collider')
            coll_victim = collision.get('victim')
            victim_speed = float(collision.get('victimSpeed'))
            collider_speed = float(collision.get('colliderSpeed'))
            time.append(coll_time)
            lane.append(coll_lane)
            pos.append(coll_pos)
            colider.append(coll_colider)
            victim.append(coll_victim)
            collider_speeds.append(collider_speed)
            victim_speeds.append(victim_speed)
        
        collision_counts[value] = {'time': time, 'lane': lane, 'pos': pos, 'colider': colider, 'victim': victim,
            'collider_speeds': collider_speeds, 'victim_speeds': victim_speeds, "total": len(time)}
        
        cols.append(len(time))

def save_and_plot_collision(collision_data):
    main_folder_name = os.path.join('plots', f'{parameter_name}')
    os.makedirs(main_folder_name, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(param_val, cols, marker='o', linestyle='-')
    plt.title(f'Total Number of Collisions vs. {parameter_name}')
    plt.xlabel(parameter_name)
    plt.ylabel('Total Number of Collisions')
    plt.grid(True)
    plt.savefig(os.path.join(f'plots/{parameter_name}', 'collision_vs_params.png'))
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.plot(param_val, brakes_counts.values(), marker='o', linestyle='-')
    plt.title(f'Number of Emergency Brakes vs. {parameter_name}')
    plt.xlabel(parameter_name)
    plt.ylabel('Number of Emergency Brakes')
    plt.grid(True)
    plt.savefig(os.path.join(f'plots/{parameter_name}', 'brakes_vs_params.png'))
    plt.close()

    for value, data in collision_data.items():
        folder_name = os.path.join(f'{main_folder_name}', f'{parameter_name}_{value}')
        os.makedirs(folder_name, exist_ok=True)

        plt.figure(figsize=(10, 6))
        plt.hist(data['pos'], bins=20, alpha=0.75, color='b', label='Position vs. Time Histogram')
        plt.title(f'Position vs. Time for {parameter_name} = {value}')
        plt.xlabel('Position (m)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig(os.path.join(folder_name, 'position_vs_time_histogram.png'))
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.boxplot([data['collider_speeds'], data['victim_speeds']], labels=['Collider Speed', 'Victim Speed'])
        plt.title(f'Collider Speed vs. Victim Speed for {parameter_name} = {value}')
        plt.xlabel('Speed Type')
        plt.ylabel('Speed (m/s)')
        plt.savefig(os.path.join(folder_name, 'speeds_boxplot.png'))
        plt.close()

        plt.figure(figsize=(10, 6))
        plt.hist(data['time'], bins=30, rwidth=0.9, alpha=0.75, label='Time vs. Number of Collisions', color='blue')
        plt.title(f'Time vs. Number of Collisions for {parameter_name} = {value}')
        plt.xlabel('Time (s)')
        plt.ylabel('Number of Collisions')
        plt.legend()
        plt.savefig(os.path.join(folder_name, 'time_vs_collisions.png'))
        plt.close()

        plt.figure(figsize=(10, 6))

        positions_by_lane = {}

        for value, data in collision_data.items():
            for lane, pos in zip(data['lane'], data['pos']):
                if lane not in positions_by_lane:
                    positions_by_lane[lane] = {'positions': [], f'{parameter_name}': []}
                positions_by_lane[lane]['positions'].append(pos)
                positions_by_lane[lane][f'{parameter_name}'].append(value)

        for lane, data in positions_by_lane.items():
            plt.scatter(data[f'{parameter_name}'], data['positions'], label=f'Lane {lane}', alpha=0.5)

        lane_counts_by_value = {}

        for value in param_val:
            param_v = collision_counts[value]['lane']
            lane_counts = {lane: param_v .count(lane) for lane in set(param_v)}
            lane_counts_by_value[value] = lane_counts

        unique_lanes = positions_by_lane.keys()

        bar_width = 0.1

        x = np.arange(len(unique_lanes))

        plt.figure(figsize=(10, 6))

        for i, value in enumerate(param_val):
            counts = [lane_counts_by_value[value].get(lane, 0) for lane in unique_lanes]
            color = plt.cm.viridis(float(i) / (len(param_val) - 1))  # Color based on index
            plt.bar(x + (i - 2) * bar_width, counts, bar_width, label=f'{parameter_name} = {value}', color=color)

        plt.title(f'Collisions in Each Lane for Multiple {parameter_name} Values')
        plt.xlabel('Lane')
        plt.ylabel('Number of Collisions')
        plt.xticks(x, unique_lanes, rotation=90)
        plt.legend()
        plt.savefig(os.path.join(f'plots/{parameter_name}', 'collision_vs_lane.png'))
        plt.close()

        plt.title(f'Position of Accidents by Lane and {parameter_name}')
        plt.xlabel(parameter_name)
        plt.ylabel('Position (m)')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(f'plots/{parameter_name}', 'positions_vs_params.png'))
        plt.close()


save_and_plot_collision(collision_counts)

