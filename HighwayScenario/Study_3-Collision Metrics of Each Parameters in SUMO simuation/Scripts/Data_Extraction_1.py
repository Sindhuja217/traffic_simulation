import os
import logging
import traci
import xml.etree.ElementTree as ET

# Configuration
SUMO_CMD = ["sumo-gui", "-c", "Highway_sumoconfig.sumocfg"]  # Use 'sumo' for non-GUI mode
ROUTES_FILE = "Highway.rou.xml"
OUTPUT_DIR = "simulation_outputs"

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def modify_routes_file(attribute_changes, vehicle_or_flow_id, type):
    tree = ET.parse(ROUTES_FILE)
    root = tree.getroot()
    print(root)
    print('Inside modify routes file')
    print('vehicle id',vehicle_or_flow_id)
    print(root.findall(f".//{vehicle_or_flow_id}"))
    print(attribute_changes.items())
    default_vehtype = root.find(".//vType[@id='DEFAULT_VEHTYPE']")
    # for elem in root.findall(f".//{vehicle_or_flow_id}"):
    # .//vType[@id='DEFAULT_VEHTYPE']
    if type == "vType":
        for elem in root.findall(f".//vType[@id='{vehicle_or_flow_id}']"):
            for attr, value in attribute_changes.items():
                print(attr,value)
                elem.set(attr, str(value))

    attr_value_pairs = "_".join([f"{k}={v}" for k, v in attribute_changes.items()])
    modified_routes_file = os.path.join(OUTPUT_DIR, f"modified_{vehicle_or_flow_id}_{attr_value_pairs}.xml")
    tree.write(modified_routes_file)
    return modified_routes_file, attr_value_pairs

def run_simulation(modified_routes_file, attr_value_pairs):
    # Update the SUMO_CMD to use the modified routes file
    output_file = os.path.join(OUTPUT_DIR, f"output_{attr_value_pairs}.xml")

    # Prepare the command with the desired output file
    cmd = SUMO_CMD + ["-r", modified_routes_file]
    cmd = cmd + ["--collision-output", output_file]
    
    traci.start(cmd)
    try:
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()
    except Exception as e:
        logging.error(f"Error during simulation: {e}")
    finally:
        traci.close()

def main():
    initialize_output_dir()

    vehicle_types = {
        "vType": {
            "DEFAULT_VEHTYPE": {"decel": [1.5, 2.0, 2.5], "accel": [3.6, 4, 4.5], "maxSpeed": [20, 25, 30], "length": [4, 5, 6], "speedFactor": [1.5, 1.9, 2.4], "jmIgnoreFoeProb": [0.5, 0.7, 0.9], "tau":[0.2, 0.3, 0.4], "sigma" :[0.6, 0.7, 0.9]},
            "EGO_VEHTYPE": {"impatience": [1.00, 0.9], "maxSpeed": [40, 45], "laneChangeModel": ["LC2013"], "lcStrategic":[-0.9,-1.0], "lcCooperative" :[-0.9,-1.0], "lcSpeedGain":[0.0,0.3], "lcPushy":[0.7,1.0], "lcImpatience":[0.5,1.0], "jmIgnoreFoeProb":[0.5,0.7,0.9], "carFollowModel":["EIDM"], "accel":[2.0,2.6], "decel":[3.0,3.5], "collisionMinGapFactor":[3.0,3.5], "tau":[0.3,0.5], "sigmagap":[0.9,0.99], "sigmaerror":[0.8,0.9], "eidmaccfactor":[1.2,1.9], "eidmdelta":[1,2], "eidmmingap":[1,1.5], "eidmtau":[0.5,0.6]}
        }
    }

    flows = {
        "flow": {
            "f_0_default": {"begin": [0.00, 1.00], "end": [200], "vehsPerHour": [600]},
            "f_1_ego": {"begin": [5.00, 6.00], "end": [200], "vehsPerHour": [600]}
        }
    }

    # Iterate over vehicle types
    for elem_name, elements in vehicle_types.items():
        for elem_id, attributes in elements.items():
            for attr, values in attributes.items():
                for value in values:
                    logging.info(f"Starting simulation for {elem_name} {elem_id} with {attr} = {value}")
                    modified_routes_file, attr_value_pairs = modify_routes_file({attr: value}, elem_id, elem_name)
                    run_simulation(modified_routes_file, attr_value_pairs)
                    logging.info(f"Completed simulation for {elem_name} {elem_id} with {attr} = {value}")

    # Iterate for flows
    for elem_name, elements in flows.items():
        for elem_id, attributes in elements.items():
            for attr, values in attributes.items():
                for value in values:
                    logging.info(f"Starting simulation for {elem_name} {elem_id} with {attr} = {value}")
                    modified_routes_file, attr_value_pairs = modify_routes_file({attr: value}, elem_id)
                    run_simulation(modified_routes_file, attr_value_pairs)
                    logging.info(f"Completed simulation for {elem_name} {elem_id} with {attr} = {value}")

if __name__ == "__main__":
    main()
