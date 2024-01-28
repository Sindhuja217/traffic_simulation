# Study 5 - Vehicle Collision Prediction based on SUMO time series data

This repository is dedicated to exploring various time series forecasting methods for predicting collision events. The project is methodically organized into three main phases: `ARIMA_collision_prediction`, `LSTM_collision_prediction`, and `VECM_collision_prediction`, each employing a different predictive model. Notably, the VECM model has demonstrated superior performance in our analysis.

## Directory Structure and Flow of Analysis

### `ARIMA_collision_prediction`
**Objective:** Utilize the ARIMA model for collision prediction.
- **Contents:** 
  - CSV datasets: `dataset_fcd_col_2.csv`, `dataset_fcd_col_3.csv`, `dataset_fcd_col_4.csv`, `train_set.csv`.
  - Jupyter notebook for ARIMA implementation (`pynb_ARIMA_30_11_23.ipynb`).
- **Usage:** Run the notebook to perform collision predictions using the ARIMA model.
- For more details on the models, and results refer to the [report_30_11_23]

### `LSTM_collision_prediction`
**Objective:** Apply LSTM (Long Short-Term Memory) networks for collision prediction.
- **Contents:**
  - LSTM analysis notebook (`Collision Prediction Timeseries LSTM.ipynb`).
  - SUMO simulation files and logs.
  - `datasets` folder with CSV files for collision and no-collision events.
  - `output` folder containing simulation results.
- **Usage:** Implement the LSTM model notebook for predicting collision events using time series data.
- For more details on the models, and results refer to the [report_7_12_23]

### `VECM_collision_prediction`
**Objective:** Implement the Vector Error Correction Model (VECM) for collision prediction.
- **Flow:** Advances to VECM following the ARIMA and LSTM analyses.
- **Contents:**
  - VECM analysis notebook (`Collision_VECM.ipynb`).
  - Relevant scripts, configuration files, and datasets for VECM analysis.
  - `output` and `VECM_analysis` subdirectories with simulation outputs and datasets.
- **Usage:** Utilize the VECM model notebook for collision prediction analysis.
- For more details on the models, and results refer to the [report_14_12_23]

[report_30_11_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_5-vehicle_collision_prediction/report_30_11_23.pdf>
[report_7_12_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_5-vehicle_collision_prediction/report_7_12_23.pdf>
[report_14_12_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_5-vehicle_collision_prediction/report_14_12_23.pdf>
