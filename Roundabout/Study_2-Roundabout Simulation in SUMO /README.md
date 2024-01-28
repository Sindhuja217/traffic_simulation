# Roundabout Simulation in SUMO 

## Overview
This SUMO simulation project presents a comprehensive study of traffic dynamics around a roundabout, focusing on collision scenarios, vehicle behavior, and traffic flow efficiency.

## Collision Scenarios
Several collision scenarios were simulated:
- **Scenario 1**: Collisions at roundabout insertion due to high vehicle flow rate.
- **Scenario 2**: Collisions during movement within the roundabout.
- **Scenario 3**: Lane changing collisions within the roundabout.
- **Scenario 4**: Junction collisions between identical vehicle types during lane changes.

## Key Output Files for Analysis
Each output file provides unique insights into the simulation:

- **FCD Output**: Details the trajectory data of vehicles, including position, speed, and heading. [FCD Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Floating_Car_Data_Output.html)
- **Collision Output**: Records information on each collision event that occurs during the simulation. [Collision Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Collision_Output.html)
- **Lane Change Output**: Documents lane change events and behaviors of vehicles. [Lane Change Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Lane-Change_Output.html)
- **Statistics Output**: Provides aggregate data on simulation performance. [Statistics Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Statistics_Output.html)
- **Summary Output**: Offers a snapshot view of the simulation's state at various moments. [Summary Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Summary_Output.html)


Data analysis focuses on parameters like position, acceleration, velocity, and time to understand vehicle behavior and traffic efficiency.

## Simulation Parameters
- **Step Length**: 0.80 seconds for frequent collision checks and better positioning.
- **Collision Action**: 'remove' to simulate the effect of vehicle removal post-collision.
- **Collision Stop Time**: 2 seconds, determining how long a vehicle stops after a collision.
- **Flow Parameters**: Different vehicle types (DEFAULT and EGO) with varied attributes.
- **Begin and End Time**: 0 to 200 seconds, setting the simulation duration.
- **Vehicles Per Hour**: 1800 vehicles/hour, influencing traffic density and collision probability.

## Resources and References
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Managing Simulation Output in SUMO](https://sumo.dlr.de/docs/Simulation/Output/index.html)
- [SUMO Collision Modeling](https://sumo.dlr.de/docs/Simulation/VehicleCollisionRemoval.html)

