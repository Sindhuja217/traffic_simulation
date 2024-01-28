# Next Step Prediction

## Overview
This project explores traffic simulation in SUMO, focusing on Lanelet2 conversion and employing various machine learning models for classification and analysis.

## Scenarios and Models

### Scenario 1: LSTM on Single Simulation Data
- **Focus**: Analyzes single simulation data using Long Short-Term Memory (LSTM) networks.
- **Key Metric**: Concentrates on 'least_distance' to assess collision risk.

### Scenario 2: LSTM on Combined Data
- **Approach**: Applies LSTM to combined datasets from multiple simulations.
- **Analysis**: Examines 'least_distance' for a comprehensive risk assessment.

### Scenario 3: ARIMA on Single Simulation Data
- **Model Used**: Autoregressive Integrated Moving Average (ARIMA) for single simulation data.
- **Metrics**: Analyzes 'relative_speed' and 'least_distance' for trend prediction.

### Scenario 4: ARIMA on Combined Data
- **Application**: Uses ARIMA on combined datasets.
- **Prediction**: Focuses on trends in 'relative_speed' and 'least_distance'.

## Data Preparation and Exploration
- **Data Processing**: Parsing XML data from simulations and merging relevant datasets.
- **Feature Engineering**: Calculation of features like acceleration, nearest vehicle distance, and relative speed.

## Results and Analysis
- **Model Performance**: LSTM and GRU models trained on single and combined simulation data.
- **Key Metrics**: Evaluation of least distance, speed, and relative speed for collision prediction.

## Resources
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
