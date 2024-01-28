import random
import os
import sumolib
import traci
import xml.etree.ElementTree as ET
import re
import csv
import json

# Define the SUMO command
sumoCmd = [sumolib.checkBinary('sumo'), '-c', 'intersec.sumocfg', '--log', 'simulation_main.log','--random']

xml_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">
    <!-- VTypes -->
    <vTypeDistribution id="vd1">
        <vType id="normal" guiShape="passenger" carFollowModel="EIDM" color="blue" probability="0.2" tau="1.5" minGap="2.5" accel="2.6" decel="4.5" sigmaerror="0.1" maxSpeed="33.33" emergencyDecel="4.5" />
        <vType id="speeder" guiShape="passenger" carFollowModel="EIDM" color="yellow" probability="0.2" tau="1.5" minGap="2.5" accel="5" decel="6" sigmaerror="0.1" maxSpeed="41.67" emergencyDecel="6" />
        <vType id="tailgater" guiShape="passenger" carFollowModel="EIDM" color="orange" probability="0.2" tau="0.1" minGap="1" accel="3" decel="5" sigmaerror="0.5" maxSpeed="33.33" emergencyDecel="7" />
        <vType id="aggressive" guiShape="passenger" carFollowModel="EIDM" color="red" probability="0.2" tau="0.1" minGap="1" accel="5" decel="5" sigmaerror="0.5" maxSpeed="41.67" emergencyDecel="7" jmDriveRedSpeed="10" jmDriveAfterRedTime="4" jmDriveAfterYellowTime="4" lcCooperative="-1" lcSpeedGain="10" />        
        <vType id="violator" guiShape="passenger" carFollowModel="EIDM" color="black" probability="0.2" tau="0.1" minGap="1" accel="3" decel="5" sigmaerror="0.5" maxSpeed="33.33" emergencyDecel="7" jmDriveAfterYellowTime="4" />
    </vTypeDistribution>
    
    <!-- Routes -->
    <routeDistribution id="rd1">
        <route id="r_0" edges="-E6 -E5 -E1 E3 E7" probability="0.2"/>
        <route id="r_1" edges="E0 E1 E5 E6" probability="0.2"/>
        <route id="r_2" edges="E2 E3 E7" probability="0.2"/>
        <route id="r_3" edges="-E7 -E3 -E0" probability="0.2"/>
        <route id="r_4" edges="-E6 -E5 -E1 -E0" probability="0.2"/>
    </routeDistribution>

    <flow id="myflow" type='vd1' route='rd1' begin="0" end="10000" number="1000">
    </flow>
</routes>
"""

collision_file = os.path.join('output', 'collisions.xml')

max_runs = 2

def simulation_sumo_intersec():
    runs = 1
    sim_internal = {}
    while runs < max_runs:
        sim_events = {"collisions":[], 'total collisions':0,"emergency brakes":0}
        with open("intersec.rou.xml", "w") as xml_file:
            xml_file.write(xml_template)

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
    return sim_internal


sim_dic = simulation_sumo_intersec()
json_file = 'simulation_output.json'

with open(json_file, "w") as json_file:
    json.dump(sim_dic, json_file)