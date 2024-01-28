import random
import os
import sumolib
import traci
import xml.etree.ElementTree as ET
import re
import csv
import json

parameter_name = os.environ.get("parameter_name", "jmIgnoreFoeProb")
param_val = os.environ.get("param_val", [0.1,0.3,0.4,0.6,0.7,0.9,1])
param_val = param_val.strip('][').split(',')
for i in range(len(param_val)):
    try:
        param_val[i] = float(param_val[i])
    except:
        continue

print(f"param_name {parameter_name} --- param_val {param_val}")

# Define the SUMO command
sumoCmd = [sumolib.checkBinary('sumo'), '-c', 'intersec.sumocfg', '--log', 'simulation_main.log','--random']

route_prob_range = (0.4, 0.6)

def random_probability(prob_range):
    return round(random.uniform(*prob_range), 1)

xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- VTypes -->
    <vTypeDistribution id="vd1">
        <vType id="ego_veh" guiShape="passenger" carFollowModel="EIDM" color="red" probability="0.5" emergencyDecel="5" />
        <vType id="default" guiShape="passenger" carFollowModel="Krauss" color="yellow" probability="0.5" />
    </vTypeDistribution>
    
    <!-- Routes -->
    <routeDistribution id="rd1">
        <route id="r_0" edges="-E1 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_1" edges="E0 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_10" edges="-E3 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_11" edges="-E1 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_2" edges="-E3 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_3" edges="E2 E3" probability="{random_probability(route_prob_range)}"/>
        <route id="r_4" edges="-E1 E3" probability="{random_probability(route_prob_range)}"/>
        <route id="r_5" edges="E2 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_6" edges="E0 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_7" edges="-E3 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_8" edges="E2 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_9" edges="E0 E3" probability="{random_probability(route_prob_range)}"/>
    </routeDistribution>

    <flow id="myflow" type='vd1' route='rd1' begin="0" end="500" number="500">
    </flow>
</routes>
"""

collision_file = os.path.join('output', 'collisions.xml')
max_runs = 11 # change the total number of runs here

def simulation_sumo_intersec():
    simulation_dic = {}
    for value in param_val:
        runs = 1
        sim_internal = {}
        while runs < max_runs:
            sim_events = {"collisions":[], 'total collisions':0,"emergency brakes":0}
            with open("intersec.rou.xml", "w") as xml_file:
                xml_file.write(xml_template)
            tree = ET.parse('intersec.rou.xml')
            root = tree.getroot()
            vtype = root.find(".//vType[@id='ego_veh']")
            vtype.set(parameter_name, str(value))
            tree.write('intersec.rou.xml')
            traci.start(sumoCmd)

            while traci.simulation.getMinExpectedNumber() > 0:
                traci.simulationStep()
            traci.close()

            with open('simulation_main.log', 'r') as log_file:
                log_content = log_file.read()
                brakes_matches = re.findall(r"Warning:.*emergency braking", log_content, re.MULTILINE)

            if os.path.exists(collision_file):
                collision_tree = ET.parse(collision_file)
                collision_root = collision_tree.getroot()
                sim_events['emergency brakes'] = len(brakes_matches)
                sim_events['total collisions'] = len(collision_root.findall('collision'))
                if collision_root.find('collision') is not None:
                    c1=0
                    for collision in collision_root.findall('collision'):
                        c1+=1
                        collision_dict = {}
                        collision_dict['time'] = float(collision.get('time'))
                        collision_dict['lane'] = collision.get('lane')
                        collision_dict['collider'] = collision.get('collider')
                        collision_dict['colliderSpeed'] = float(collision.get('colliderSpeed'))
                        collision_dict['colliderType'] = collision.get('colliderType')
                        collision_dict['pos'] = float(collision.get('pos'))
                        collision_dict['type'] = collision.get('type')
                        collision_dict['victim'] = collision.get('victim')
                        collision_dict['victimSpeed'] = float(collision.get('victimSpeed'))
                        collision_dict['victimType'] = collision.get('victimType')
                        sim_events['collisions'].append(collision_dict)
                    sim_internal[runs] = sim_events
                else:
                    sim_internal[runs] = sim_events
            runs+=1
        simulation_dic[value] = sim_internal

    return simulation_dic


sim_dic = simulation_sumo_intersec()
json_file = os.path.join('simulation_output_json/json_files_50',f'simulation_output_{parameter_name}.json') # change this to simulation_output_json/json_files_30 for 30% ego cars json directory

with open(json_file, "w") as json_file:
    json.dump(sim_dic, json_file)