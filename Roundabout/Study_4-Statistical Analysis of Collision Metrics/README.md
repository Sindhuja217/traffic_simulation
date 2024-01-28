# Statistical Analysis of Collision Metrics 

## Overview
This project explores the impact of varying vehicle parameters on traffic behavior in a SUMO-simulated roundabout environment. It focuses on analyzing different driving behaviors and their influence on traffic dynamics and safety.

## Simulation Parameters
The simulation includes two distinct vehicle types (DEFAULT and EGO) with varied attributes such as `tau`, `collisionMinGapFactor`, `sigmagap`, `sigmaerror`, and `lcCooperative`. Key parameters are adjusted to study their effect on traffic behavior and safety:
- **Vehicle Types**: DEFAULT_VEHTYPE and EGO_VEHTYPE, each with unique characteristics.
- **Flow IDs**: Four distinct flows (`f_0_default`, `f_1_default`, `f_0_ego`, `f_1_ego`) defining the routes and vehicle types.
- **Time Parameters**: Begin at 0.00s and end at 200.00s to capture a comprehensive traffic pattern.
- **Vehicles Per Hour**: Set at 600 for each flow to maintain consistent traffic density.

## Collision Scenarios and Data Analysis
Two main scenarios are studied:
- **Scenario 1**: Examines the mean and variance of collisions for each parameter across multiple simulation runs.
- **Scenario 2**: Compares traffic dynamics of four distinct driving behaviors (Passive Drivers, Aggressive Drivers, Tailgaters, Speeders) across two routes.

Data analysis focuses on collision counts, rates, and the impact of varied driving behaviors on traffic safety.

## Key Output Files for Analysis
- **CollisionMinGapFactor**: Analyzes the impact of gap factor on collision frequency.
- **Tau**: Studies the effect of reaction time on traffic flow and collisions.
- **SigmaGap and SigmaError**: Examines the influence of perception variability on driving behaviors and collision rates.
- **LcCooperative**: Assesses how cooperative behavior during lane changing affects traffic safety.

## Resources and References
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Vehicle Types and Parameters in SUMO](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
- [Traffic Flow and Collision Analysis in SUMO](https://sumo.dlr.de/docs/Simulation/VehicleCollisionRemoval.html)

