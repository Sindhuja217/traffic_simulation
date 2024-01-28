import random
import os
import sumolib
import traci
import xml.etree.ElementTree as ET
import re
import csv
import json
import sys
import numpy as np
import statistics
import math

param_json = sys.argv[1]
with open(param_json, 'r') as json_file:
    param_dic_vals= json.load(json_file)

decel = np.array([param_dic_vals[vals]['decel'] for vals in param_dic_vals.keys()]) # keep this variable if you have included decelaration in the parameters.json file

# parameters that are used in combination with other parameters (check report for more details)
max_speed = 41.67
emergencyDecel = [*decel + 2] # change the value of emergency decelaration accordingly. Keep this variabel if you have included decelaration in the parameters.json file
sigmaerror = 0
tau = 0.1

# SUMO command
sumoCmd = [sumolib.checkBinary('sumo'), '-c', 'intersec.sumocfg', '--log', 'simulation_main.log','--random']

route_prob_range = (0.3, 0.7)

def random_probability(prob_range):
    return round(random.uniform(*prob_range), 1)

xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- VTypes -->
    <vTypeDistribution id="vd1">
        <vType id="ego_veh" guiShape="passenger" carFollowModel="EIDM" color="red" probability="0.5" />
        <vType id="default" guiShape="passenger" carFollowModel="Krauss" color="yellow" probability="0.5" />
    </vTypeDistribution>
    
    <!-- Routes -->
    <routeDistribution id="rd1">
        <route id="r_0" edges="-E1 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_1" edges="E0 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_2" edges="-E3 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_3" edges="-E1 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_4" edges="-E3 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_5" edges="E2 E3" probability="{random_probability(route_prob_range)}"/>
        <route id="r_6" edges="-E1 E3" probability="{random_probability(route_prob_range)}"/>
        <route id="r_7" edges="E2 E1" probability="{random_probability(route_prob_range)}"/>
        <route id="r_8" edges="E0 -E2" probability="{random_probability(route_prob_range)}"/>
        <route id="r_9" edges="-E3 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_10" edges="E2 -E0" probability="{random_probability(route_prob_range)}"/>
        <route id="r_11" edges="E0 E3" probability="{random_probability(route_prob_range)}"/>
    </routeDistribution>

    <flow id="myflow" type='vd1' route='rd1' begin="0" end="200" number="100">
    </flow>
</routes>
"""

collision_file = os.path.join('output', 'collisions.xml')

max_runs = 6
def simulation_sumo_intersec():
    simulation_dic = {}
    for vals,emdecel in zip(param_dic_vals.values(),emergencyDecel):
        sim_events = {'total collisions':0,"emergency brakes":0}
        runs = 1
        cols = []
        embrakes = [] 
        while runs < max_runs:
            with open("intersec.rou.xml", "w") as xml_file:
                xml_file.write(xml_template)
            tree = ET.parse('intersec.rou.xml')
            root = tree.getroot()
            vtype = root.find(".//vType[@id='ego_veh']")

            # change the values of the parameters based on parameters.json file
            vtype.set('accel', str(vals['accel']))
            vtype.set('decel', str(vals['decel']))
            vtype.set('tau', str(tau))
            #vtype.set('minGap', str(minGap))
            vtype.set('sigmaerror', str(sigmaerror))
            vtype.set('emergencyDecel', str(emdecel))
            vtype.set('maxSpeed', str(max_speed))

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
                cols.append(len(collision_root.findall('collision')))
                embrakes.append(len(brakes_matches))
            runs+=1
        sim_events['total collisions'] = math.ceil(statistics.mean(cols))
        sim_events['emergency brakes'] = math.ceil(statistics.mean(embrakes))
        simulation_dic[f"{vals}"] = sim_events
    return simulation_dic

sim_dic = simulation_sumo_intersec()
json_file = os.path.join('simulation_op','simulation_output_check.json') # change the name of the json file accordingly

with open(json_file, "w") as json_file:
    json.dump(sim_dic, json_file)