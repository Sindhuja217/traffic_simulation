# lanelet2 Representation of FCD Data

## Highway Road Network Details
- **Focus**: Simulation of a highway road network in London's Highbury Avenue using SUMO.
- **Features**: Includes traffic signals, walkways, and various road lanes.

## Conversion of SUMO .Net File to Lanelet2 Format
- **Objective**: Transforming SUMO traffic networks for autonomous driving simulation applications.
- **Tools Used**: SUMO, OpenDRIVE, Lanelet2, and CommonRoad Designer.
- **Process**:
  - From SUMO to OpenDRIVE: Conversion using `netconvert` for detailed road network representation.
  - From OpenDRIVE to CommonRoad: Importing and adapting road networks for scenario visualization.
  - From CommonRoad to Lanelet2: Conversion script for detailed lane and traffic rule mapping.

## Methodology
- **Step-by-Step Conversion**: Ensuring preservation of road network features across various formats.
- **Data Accuracy and Integrity**: Critical for the simulation and analysis of traffic networks.

## Lanelet2 Format
- **Structure**: Detailed representation of road networks using OSM format.
- **Elements**:
  - Nodes: Define coordinates of specific locations.
  - Ways: Represent linear features like roads and lanes.
  - Relations: Organize elements into complex structures.
  - Tags: Provide descriptive information about road network features.

## Generation and Conversion of FCD Output
- **FCD Extraction**: Using SUMO to obtain detailed vehicle data.
- **Conversion to Latitude and Longitude**: For integration with GIS or mapping services.
- **Linking Vehicles to Road Network**: Assigning nodes, ways, and lanelets to vehicles in the FCD XML file.

## Conclusion
The report details the intricate process of converting and analyzing traffic simulation data, essential for understanding vehicle dynamics in urban environments.

## For more details and better understanding,please refer to report [report_14-11-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_10-Lanelet2_Representation/report_14-11-2023.pdf)

## Links reffered
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage discription of the simulator
- [Netconvert](https://sumo.dlr.de/docs/netconvert.html) - imports digital road networks from different sources and generates road networks that can be used by other tools from the package.
- [Common Road Scenario](https://commonroad-scenario-designer.readthedocs.io/en/latest/details/commonroad_scenario_designer/) - The CommonRoad Scenario Designer is a graphical user interface (GUI), which integrates all currently developed converters with and functionalities to edit and create new maps and test scenarios for motion planning of autonomous vehicles.


[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output xml]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>
