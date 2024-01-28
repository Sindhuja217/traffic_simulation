# Collision Metrics of Each Parameter in SUMO Simulation

## Overview
This project explores traffic dynamics around a roundabout using SUMO. It focuses on varying parameters to analyze collision data, emphasizing real-world traffic scenarios and vehicle interactions within a simulated environment.

## Simulation Parameters
Key parameters include:
- **Step Length**: 0.80 seconds for detailed vehicle movement analysis.
- **Collision Action**: 'remove', simulating vehicle removal after collisions.
- **Collision Stop Time**: 2 seconds, indicating post-collision vehicle halt duration.
- **Begin and End Time**: Simulation spans from 0 to 200 seconds.

## Collision Scenarios and Analysis
The study examines different collision scenarios, assessing factors like vehicle types, traffic flow, and specific parameters like `tau`, `collisionMinGapFactor`, `sigmaerror`, `sigmagap`, and `lcooperative`. Analysis includes:
- **Position Analysis**: Identifying high-risk areas within the roundabout.
- **Acceleration and Velocity**: Studying vehicle speed dynamics and their impact on collisions.
- **Time Analysis**: Observing collision patterns over different time frames.

## Data Collection and Analysis
Data is collected through various output files, providing insights into traffic behavior and safety:
- **FCD Output**: [FCD Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Floating_Car_Data_Output.html)
- **Collision Output**: [Collision Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Collision_Output.html)
- **Lane Change Output**: [Lane Change Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Lane-Change_Output.html)
- **Statistics Output**: [Statistics Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Statistics_Output.html)
- **Summary Output**: [Summary Output Documentation](https://sumo.dlr.de/docs/Simulation/Output/Summary_Output.html)

## Resources and References
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Managing Simulation Output in SUMO](https://sumo.dlr.de/docs/Simulation/Output/index.html)
- [SUMO Collision Modeling](https://sumo.dlr.de/docs/Simulation/VehicleCollisionRemoval.html)
