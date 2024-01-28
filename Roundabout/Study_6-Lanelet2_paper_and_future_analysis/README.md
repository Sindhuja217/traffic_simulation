# Lanelet2_paper_and_future_analysis 

## Overview
This project utilizes SUMO to simulate traffic around a roundabout, with a focus on integrating Lanelet2 for enhanced map details and employing predictive models for collision detection. It explores the effectiveness of various algorithms in predicting traffic incidents in detailed simulated environments.

## Lanelet2 Overview
Lanelet2 is a high-definition map format crucial for autonomous driving simulations. It provides detailed lane-level information, essential for accurate vehicle positioning and movement in SUMO simulations.
- [Lanelet2 Paper](https://www.mrt.kit.edu/z/publ/download/2018/Poggenhans2018Lanelet2.pdf)

## Predictive Collision Models
We apply various predictive models including Linear Regression, Decision Trees, Random Forests, and Neural Networks to forecast potential collision points in the simulation.
- **Models Focus**: Linear Regression, Decision Trees, Random Forests, GBMs (e.g., XGBoost, LightGBM), Neural Networks (e.g., LSTM, GRU), SVM, KNN.
- **Objective**: To predict collision occurrences based on vehicle dynamics and environmental conditions within the simulation.

## Simulation Parameters and Data Analysis
- **Vehicle Dynamics**: Speed, lane position, and other critical attributes.
- **Environmental Factors**: Lane changes, vehicle density, and average speed of nearby vehicles.
- **Data Analysis**: Emphasis on collision patterns and the impact of driving behaviors on traffic safety.

## Resources and References
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Vehicle Types and Routes in SUMO](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
- [SUMO Netedit](https://sumo.dlr.de/docs/Netedit/index.html)
- [Lanelet2 Paper](https://www.mrt.kit.edu/z/publ/download/2018/Poggenhans2018Lanelet2.pdf)

