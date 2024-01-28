# Statistical Analysis of Collision Metrics

## Objective
This focuses on conducting multiple traffic simulations in SUMO, altering various parameters like tau, collisionmingap, sigmaerror, and emergency deceleration to examine the outcomes, especially regarding collision-related data using mean and variance statistics.

## Vehicle Types and Flows
Defined vehicle types ('vType') and traffic flows ('flow') in SUMO simulations:

1. **DEFAULT_KRAUSS**: Represents a yellow vehicle, designed to avoid collisions.
2. **DEFAULT_VEHTYPE**: Represents a red vehicle, designed with a higher likelihood of causing collisions.

Total of 10 vehicle flows are defined, comprising mixes of both DEFAULT_KRAUSS and DEFAULT_VEHTYPE vehicles.

## Scenarios

## Scenario 1 - Parameter Analysis
In-depth analysis of collisions between Default and ego vehicles on a highway, altering one simulation attribute at a time to identify the responsible parameters for collisions.

### Results
- **CollisionMinGapFactor**: Analyzed through heatmap and bar plots, showing varying collision counts with different parameter values.
- **Sigma Error**: Demonstrated a positive correlation between higher sigma error values and increased collision rates.
- **EmergencyDecel**: Slight influence on collision outcomes, with minor variations in mean and variance of collision occurrences.
- **Tau**: Inverse relationship with collision count; higher Tau values lead to fewer collisions.

## Scenario 2 - Vehicle Type Variation
Variation of specific parameters within the Intelligent Driver Model (IDM) to represent different driver behaviors:

- **Desired Speed (vdes)**
- **Minimum Headway Distance (dmin)**
- **Desired Time Headway (τ)**
- **Maximum Acceleration (amax)**
- **Comfortable Deceleration (bcomf)**

### Sumo Configuration
Defined characteristics and behavior of different vehicle types within the simulation.

### Collision Trends
- **Aggressive Vehicles**: More collisions with increased traffic congestion.
- **Tailgater Vehicles**: Similar trend to aggressive vehicles with an increase in collision counts.
- **Passive Vehicles**: Lack of collision data.
- **Speeder Vehicles**: Low collision counts in low to moderately congested traffic; data beyond 30 vehicles is lacking.

## Key Takeaways
Aggressive and tailgater vehicles tend to be involved in more collisions as traffic increases. The behavior of passive and speeder vehicles requires further data for comprehensive analysis.


## For more details and better understanding,please refer to report [report_19-10-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_4-Statistical_Analysis_of_Collision_Metrics/report_19-10-2023.pdf)
---
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

