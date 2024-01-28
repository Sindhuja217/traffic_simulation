# Lanelet2 Paper

## Lanelet2 Paper Overview

### Introduction to Lanelet2 Framework
- **Objective**: Introduces Lanelet2, a C++ open-source map framework designed for highly automated driving.
- **Need for HAD Maps**: Emphasizes the necessity for detailed road environment data, like bicycle lanes and traffic signs, crucial for automated vehicles.

### Challenges in Existing Map Formats
- **Analysis of Current Formats**: Critiques existing map formats by major providers and their limitations.
- **Need for Standardized Formats**: Highlights the absence of a widely accepted map standard for automated driving.

### Requirements for HAD Maps
- **Key Application Categories**: Categorizes map requirements into road network, lane and environment, and physical elements, stressing on precise knowledge of traffic rules and detailed lane geometry.

### Lanelet2 Framework Overview
- **Layers**: Distinguishes between the physical layer, the relational layer, and the topological layer.
- **XML-Based OSM Format**: Ensures data interchangeability and supports flat ground plane projections and height information.

### Components and Modules of Lanelet2 Framework
- **Lanelet Primitives**: Describes elements like points, linestrings, lanelets, areas, and regulatory elements.
- **Key Modules**: Includes Traffic Rules, Physical, Routing, Matching, Projection, and Input/Output Modules.

## Predictive Models for SUMO Output Data

### Model Overview
- **LSTM Networks**: For handling time-stamped data sequences in SUMO.
- **Random Forest**: Captures complex interactions in parameters like vehicle positions and environmental conditions.
- **SVM**: Manages high-dimensional data for classification tasks.
- **XGBoost**: Addresses feature interactions and complex relationships.
- **RNN**: Analyzes historical sequences of events leading to collisions.

### Logistic Regression Model
- **Features**: Includes vehicle coordinates, speed, driving behavior types, lane positioning, and collision indicators.
- **Analysis**: Demonstrates high precision and recall for non-event occurrences; however, it needs improvements in capturing positive class instances.

---
## For more details and better understanding,please refer to report [report_2-11-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_6-Lanelet2_Paper_and_future_analysis/report_2-11-2023.pdf)

## Links reffered
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage discription of the simulator
- [Lanelet2 Paper](https://www.mrt.kit.edu/z/publ/download/2018/Poggenhans2018Lanelet2.pdf) - Paper on Lanelet2 library
- [Lanelet2 library](https://github.com/fzi-forschungszentrum-informatik/Lanelet2) - Lanelet2 is a C++ library for handling map data in the context of automated driving


[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output xml]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>

