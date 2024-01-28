# Weekly Updates (19/10/2023) – Krishna Tarun Saikonda

## Objective
The focus of this week's update is on analyzing various driver behaviors in a simulated environment by customizing different vehicle types with unique parameters. This approach helps in understanding the impact of changes in acceleration, deceleration, speed, and other attributes on driver behavior and traffic flow dynamics.

## Vehicle Type Parameters
The simulation includes several distinct vehicle types, each defined by specific parameters to represent different driver behaviors:

- **AggressiveDriver**
- **CautiousDriver**
- **EcoFriendlyDriver**
- **RecklessDriver**
- **DefensiveDriver**
- **HumanLikeDriver**
- **DeliveryTruck**
- **SchoolBus**
- **AggressiveLanechangingDriver**
- **AggressiveJunctionDriver**
- **InexperiencedDriver**
- **ElderlyDriver**
- **SportsCarDriver**
- **Motorcycle**

Each vehicle type has its own set of parameters like `Car Follow Model`, `Sigma`, `Tau`, `Accel`, `Decel`, `Max Speed`, `Collision Min Gap Factor`, and `Lane Change Model`. Additional parameters like `LC Accel Lat`, `LC Assertive`, `LC Pushy`, `LC Impatience`, `LC Sigma`, `LC Speed Gain`, `LC Strategic`, `Impatience`, `jmSigmaMinor`, `jmIgnoreFoeSpeed`, `jmIgnoreFoeProb`, and `jmTimegapMinor` further characterize specific behaviors.



## Collision Analysis Visualization
To understand the frequency and concentration of collisions on the road network, various visualizations are employed:

- HeatMap of the collisions overlayed on the road network.
- Usage of Hist2d, hexbin, scatter, contour, and kdeplot for detailed analysis.

## Collision Output Analysis
The analysis includes:

- Count plot of Vehicle Types.
- Count of Collision Types.
- Collisions by Position Range.
- Histogram of Collision Speeds (0 to 70).
- Collision Counts by Lane.

## For more details and better understanding,please refer to report [report_26-10-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_5-Collision_Output_Analysis/report_26-10-2023.pdf)

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
