# Next_Step_Prediction

## Main Theme
The primary objective is to predict the next step of the 'ego_vehicle' in simulation to determine potential collisions with other vehicles.

## Vehicle Attributes
Investigation into 'default' and 'ego_vehicle' types, focusing on unique attributes like speed and acceleration.

## Data Preprocessing
Details the extraction and integration process of Floating Car Data (FCD), enhancing it with new attributes for predictive analysis.

## Scenarios and Models
### Scenario 1: LSTM on Single Simulation Data
- Analyzes single simulation data using LSTM, focusing on 'least_distance' for collision risk assessment.

### Scenario 2: LSTM on Combined Data
- Applies LSTM to combined datasets from multiple simulations, examining 'least_distance'.

### Scenario 3: ARIMA on Single Simulation Data
- Utilizes ARIMA model for single simulation data, analyzing 'relative_speed' and 'least_distance'.

### Scenario 4: ARIMA on Combined Data
- Uses ARIMA on combined datasets, predicting 'relative_speed' and 'least_distance' trends.

## Conclusion
The report demonstrates the use of LSTM and ARIMA models to predict the 'ego_vehicle's' next move, crucial for assessing collision risks in traffic simulations.

## For more details and better understanding,please refer to report [report_7-12-23](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_9-Next_Step_Prediction/report_7-12-23.pdf)

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
