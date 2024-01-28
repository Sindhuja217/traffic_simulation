# HighWay Road Network simulation in SUMO

## Overview
I focused on creating three distinct collision scenarios in a SUMO simulation environment using the Enhanced Intelligent Driver Model (EIDM) car following model. Each scenario was designed to explore specific collision dynamics and their consequences. 

## Collision Scenarios and Data Collection

### Scenario Descriptions
- **Scenario 1**: Studying Rear-End Collisions in Highway Simulation using EIDM.
- **Scenario 2**: Analyzing Lane Change Collisions in Highway Simulation with EIDM.
- **Scenario 3**: Examining Junction Collisions in Highway Simulation using EIDM.

For more details on the scenrarios and vehicle parameters reffer the [report_5_10_23]

### Data Collection
Comprehensive data was captured in XML and CSV formats, covering the following aspects:

#### Collision Outputs
Tracking collision data including the time and location of collisions in the simulation. [More Info](https://sumo.dlr.de/docs/Simulation/Output/Collisions.html)

#### Trajectory Outputs
Capturing the type, current speed, and acceleration of each vehicle. [More Info](https://sumo.dlr.de/docs/Simulation/Output/AmitranOutput.html)

#### Statistical Output
Covering various attributes related to performance, safety, and vehicle statistics. [More Info](https://sumo.dlr.de/docs/Simulation/Output/StatisticOutput.html)

#### Lane Change Output
Tracking all events of lateral vehicle lane changes and the reasons for these maneuvers. [More Info](https://sumo.dlr.de/docs/Simulation/Output/Lanechange.html)

## Simulation Adjustments

### Simulation Parameters
- **Step-length**: 0.10 seconds for simulation steps.
- **Collision.action**: Set to "remove" for post-collision actions.
- **Collision.stoptime**: 30 seconds post-collision.
- **Collision.check-junctions**: Enabled.
- **Begin and End Time**: From 0 to 1000 units.
- **Max-num-vehicles**: Maximum of 20 vehicles in the simulation.

### Flow Attributes
Significant modifications were made to vehicle insertion, positioning, and speeds within the simulation for controlled experiments.

## Specific Scenarios

### Scenario 1: Rear-End Collisions
- **VType parameter adjustments**: Fine-tuned to simulate the impact of reckless driving behavior leading to a collision.

### Scenario 2: Lane Change Collisions
- **VType parameter adjustments**: Focused on the dynamics of collisions during lane changes.

### Scenario 3: Junction Collisions
- **VType parameter adjustments**: Created to explore the conditions contributing to collisions at junctions.

## Data Analysis

### Position, Acceleration, and Velocity vs. Time
Collected detailed data on vehicle dynamics for further analysis using FCD output, aiming to understand changes in vehicle behavior during the simulation.

## For more details and better understanding,please refer to report [report_5-10-2023]

## Conclusion
The simulations provided valuable insights into collision dynamics under various scenarios, enhancing our understanding of traffic safety and behavior in simulated environments.

## Links reffered
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage discription of the simulator




[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output xml]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>


