# Study 2 - Exploring  Vehicle Parameters
Ablation studies of vehicle parameters on single simulation on SUMO simulator. 

## Scenarios
Designed 2 scenarios in SUMO for the Ablation studies, based on (30%, and 50% not following rules i.e. these vehicles will have parameters changed)
1. Scenario 1: Junction with priority 1-lane 4-way intersection. [changing one parameter at a time]
2. Scenario 2: Junction with priority 1 lane 4-way intersection. [keeping one parameter constant and checking 
the trend]

For more details on the scenarios and vehicle parameters refer to the [report_12_10_23]

## Requirements:
- [SUMO simulator]

## About Python file
The Python script [sim.py] executes the SUMO simulation for each set of parameters and their corresponding values provided by you. It runs these simulations iteratively through the command line. After each simulation, the script generates bar charts and line plots, saving them automatically in the plots folder. Within this folder, there are subfolders named after each parameter, where all related plots are stored. 
Note: I didn't include the **plots** folder, but you don't need to create **plots** folder, the code will do it automatically. 

## How to run
To test a specific vehicle parameter using a command line, choose a parameter and its corresponding values, then modify the **parameter_name** and **parameter_val** in the command appropriately. Once adjusted, execute this command in your command line in the directory where [sim.py] is present. Below is the example cmd to execute. For 30% ego vehicle reduce the flow vehicle statement of type="ego_veh" to 2 from 5 in the [route file].
```sh
export parameter_name="jmIgnoreFoeProb" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python sim.py
```
## Links Referred
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information

[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[report_12_10_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_2-exploring_vehicle_param/report_12_10_23.pdf>
[sim.py]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_2-exploring_vehicle_param/sim.py>
[SUMO simulator]: <https://eclipse.dev/sumo/>
[route file]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_2-exploring_vehicle_param/intersec_1.rou.xml>
