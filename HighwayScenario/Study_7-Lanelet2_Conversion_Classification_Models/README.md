# Lanelet2 Conversion Classification Models

## Overview
This report presents the transformation of traffic networks from SUMO XML format to OpenDrive, then to Lanelet2, and visualizing with Common Road and JSOM. It aims to facilitate the use of traffic network data across various platforms for autonomous vehicle development. Additionally, the report explores machine learning models for classifying vehicles using Floating Car Data (FCD) and other datasets.

## Lanelet2 Conversion
- **Purpose**: Providing detailed road infrastructure representation, crucial for autonomous vehicle development.
- **Process**: Involves converting SUMO .net files to Lanelet2 using Command Road Designer.
- **Lanelet2 Features**: Includes nodes, ways, relations, and tags to describe road features in detail.

## Methodology
- **Tools Used**: SUMO .net file, Lanelet2 format, and Command Road Designer.
- **Conversion Steps**: Preparing the SUMO .net file, using Command Road Designer for transformation, and generating Lanelet2's OSM format.

## Scenario Analysis
- **Scenario 2**: Predicting vehicle types using FCD output aggregation (mean, standard deviation, variance).
- **Scenario 3**: Classification using only FCD output.
- **Scenario 4**: Combining FCD output with additional extracted features for improved classification.

### Classification Models and Features
- **Models Used**: Random Forest, Deep Neural Networks (DNN), K-Nearest Neighbors (KNN), Gaussian Naive Bayes.
- **Features**: Time, ID, coordinates, angle, type, speed, position, acceleration, and additional context-specific features.

### Results
- **Random Forest Performance**: Consistently high accuracy across scenarios, especially when using additional relevant features.
- **Model Application on Unseen Data**: Random Forest demonstrates varying degrees of accuracy, suggesting the importance of feature selection and model robustness.

### Analysis
- **Model Efficacy**: Random Forest outperforms other models, with higher accuracy when supplemented with additional features.
- **Scenario Comparisons**: Shows the value of integrating a broader set of data beyond raw FCD output for accurate vehicle classification.

## For more details and better understanding,please refer to report [report_9-11-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_7-Lanelet2_Conversion_Classification_Models/report_9-11-2023.pdf)

## Links reffered
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage description of the simulator
- [Netconvert](https://sumo.dlr.de/docs/netconvert.html) - imports digital road networks from different sources and generates road networks that can be used by other tools from the package.
- [Common Road Scenario](https://commonroad-scenario-designer.readthedocs.io/en/latest/details/commonroad_scenario_designer/) - The CommonRoad Scenario Designer is a graphical user interface (GUI), which integrates all currently developed converters with and functionalities to edit and create new maps and test scenarios for motion planning of autonomous vehicles.



[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output xml]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>


