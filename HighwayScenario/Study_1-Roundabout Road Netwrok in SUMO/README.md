# # Roundabout Traffic Simulation in SUMO

"Simulation of Urban Mobility" ([SUMO]) is a versatile, open-source traffic simulation tool that offers microscopic and continuous modeling capabilities, specifically engineered to manage extensive network systems.

## Scenarios

This scenario demonstrates the creation and simulation of a roundabout traffic network using SUMO (Simulation of Urban MObility), an open-source, highly portable, microscopic, and continuous road traffic simulation package. To design the network, the Netedit tool was utilized, which is a component of the SUMO suite designed for the creation and modification of road networks.

## Methodology

1. **Network Design**: Using Netedit, a roundabout was created with multiple entry and exit points. Attention was paid to realistic lane configurations and traffic signal systems.

2. **Traffic Demand**: Traffic demand patterns were defined to simulate peak and off-peak traffic conditions. This included varying vehicle types, such as cars, buses, and trucks.

3. **Simulation**: The designed network was imported into SUMO, where various simulation parameters were set. This included time steps, vehicle speeds, and routing algorithms.

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
