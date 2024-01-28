# Collision Output Analysis in SUMO 

## Overview
This SUMO project investigates diverse driving behaviors in traffic simulation, emphasizing realistic modeling of various driver types including aggressive, passive, tailgater, speeder, distracted, inexperienced, and default drivers.

## Simulation Parameters
- **Vehicle Types**: Seven distinct types, each with unique driving characteristics.
- **Parameter Variations**: Adjustments in acceleration, deceleration, emergency deceleration, and time headway (tau) across different driver behaviors.

## Collision Scenarios and Analysis
- **Exit Collisions**: Analysis focuses on interactions between aggressive and tailgater drivers with other vehicles at roundabout exits, considering factors like deceleration and following distance.
- **Driving Behavior Impact**: Examining how aggressive driving and exit path misjudgment increase collision risks.
- **Inter-Vehicle Interaction**: Assessing the impact of different driver types on roundabout exit safety.
- **Chain-Reaction Accidents**: Potential for multi-vehicle collisions due to close-following behavior of certain driver types.

## Key Output Files for Analysis
- **Collision Data**: Insights into collision frequency and patterns.
- **Vehicle Behavior**: Analysis of driving styles and their impact on roundabout safety.

## Resources and References
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Vehicle Types and Behavior](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
- [Collision Modeling in SUMO](https://sumo.dlr.de/docs/Simulation/VehicleCollisionRemoval.html)
