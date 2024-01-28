# Study 1 - Exploring  SUMO Simulator

"Simulation of Urban Mobility" ([SUMO]) is a versatile, open-source traffic simulation tool that offers microscopic and continuous modeling capabilities, specifically engineered to manage extensive network systems.

## Requirements
- [SUMO simulator] 

## Scenarios
I simulated five collision scenarios in SUMO, all involving accidents caused by an EGO VEHICLE.
1. [Scenario 1]: 3 Lane 4 Way intersection (with TRAFFIC LIGHTS) collision at an intersection
by an EGO-VEHICLE (Krauss Car following model) that doesn’t follow traffic rules.
2. [Scenario 2]: 3 Lane 4 Way intersection (with TRAFFIC LIGHTS) rear collision at lane by
an EGO-VEHICLE (EIDM car following collision parameters) with set collision
parameters.
3. [Scenario 3]: 1 Lane 4 Way intersection (with RIGHT-OF-WAY) collision at the junction
by an EGO-VEHICLE (Junction collision and EIDM collision parameters).
4. [Scenario 4]: 3 Lane 4 Way intersection (with TRAFFIC LIGHTS) collision at the junction
by an EGO-VEHICLE (Junction collision and EIDM collision parameters) but EGOVEHICLES follow traffic rules.
5. [Scenario 5]: 3 Lane 4 Way intersection (with TRAFFIC LIGHTS) rear collision due to lane
change by an EGO-VEHICLE (EIDM and Lane change collision parameters).

For more details on the scenarios and vehicle parameters refer the [report_5_10_23]

## Links Referred
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage description of the simulator

Note: I didn't include all the CSV files that were converted from the XML files to conserve repository space. However, you can convert these files using the [xml2csv] Python script provided by SUMO. Additionally, I removed the [Full output XML] files from all scenarios due to their substantial file size.


[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Scenario 1]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/tree/main/Intersection/Study_1-exploring_SUMO/scenario_1>
[Scenario 2]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/tree/main/Intersection/Study_1-exploring_SUMO/scenario_2>
[Scenario 3]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/tree/main/Intersection/Study_1-exploring_SUMO/scenario_3>
[Scenario 4]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/tree/main/Intersection/Study_1-exploring_SUMO/scenario_4>
[Scenario 5]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/tree/main/Intersection/Study_1-exploring_SUMO/scenario_5>
[report_5_10_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_1-exploring_SUMO/report_5_10_23.pdf>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output XML]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>
[SUMO simulator]: <https://eclipse.dev/sumo/>
