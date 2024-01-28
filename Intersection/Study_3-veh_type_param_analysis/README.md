# Study 3 - Vehicle (driver) parameter and type analysis

This directory contains simulation outputs and analysis related to vehicle parameters and type analysis. It is systematically structured to follow a logical flow from P1 to P5, each focusing on different yet interconnected aspects of vehicle analysis. The content within each part builds upon the insights and data gathered in the preceding sections.

## Requirements:
- [SUMO simulator]
- shell

## Directory Structure and Analysis Flow

### `P1_vehicle_param_univariate_analysis`
**Objective:** Perform univariate analysis of vehicle parameters.
- **Flow:** Establishes the base for the analysis, focusing on individual vehicle parameters.
- **Contents:** 
  - `output`: Analysis results with collision XML file.
  - `simulation_output_json`: JSON formatted simulation data with subdirectories for different parameter sets (`json_files_30`, `json_files_50`) and plots (`output_plot_30`, `output_plot_50`). Where 30 and 50 represent the percentage of ego vehicles in simulation.
  - `run_sim_imp.sh` run the simulation for all parameters and their corresponding list, you can add more parameters to test you can find some shell statements for other parameters in `run_param_sim.sh`
  - `run_plots.sh` shell script to make parameter plots in simulation_output_json folder
 - **How to run**
    cmd to run simulation for all parameter
     ```sh
    ./run_sim_imp.sh
    ```
    cmd to generate plots from the JSON outputs
     ```sh
    ./run_plots.sh
    ```
- For more details on the scenarios and vehicle parameters refer to the [report_19_10_23]

### `P2_vehicle_type_analysis`
**Objective:** Analyze different vehicle types.
- **Flow:** Extends `P1`'s insights to various vehicle types. [Paper implementation and custom scenario implementation]
- **Contents:** 
  - `output`: Analysis results with collision XML file.
  - `output_plot`: Visualizations divided into `paper_implementation` and `scene_1`.
  - `param_sim_json.py`: runs the simulation and stores collision-related data in simulation_output.json
  - `plots.py`: plots generated using the simulation_output.json
 - **How to run**
    cmd to run simulation for all parameter
     ```sh
    python param_sim_json.py
    ```
    cmd to generate plots from the JSON outputs
     ```sh
    python plots.py output_plot/scene_1
    ```
- For more details on the scenarios and vehicle parameters refer to the [report_19_10_23]

### `P3_vehicle_param_multivariate_analysis`
**Objective:** Conduct multivariate analysis of vehicle parameters considering practical real road parameter values.
- **Flow:** Integrates multiple vehicle parameters.
- **Contents:** 
  - `simulation_op`: Simulation outputs of parameter analysis.
  - `parameters.json`: accel and decel parameters
  - `Parameter Analysis.ipynb`: pynb to make plots
 - **How to run**
    cmd to run simulation for parameters in parameters.json
     ```sh
    python param_sim_json.py parameters.json
    ```
- For more details on the scenarios and vehicle parameters refer to the [report_26_10_23]
- You can change the parameters of JSON file based on the type variable you want to analyze.

### `P4_vehicle_type_interaction`
**Objective:** Explore interactions between different vehicle types considering practical real road parameter values.
- **Flow:** Applies findings from `P2` and `P3` to study vehicle type interactions.
- **Contents:** 
  - `output_plot`: Interaction visualizations among different vehicle types.
 - **How to run**
    cmd to run the simulation
     ```sh
    python param_sim_json.py
    ```
    cmd to generate plots from the JSON outputs
     ```sh
    python plots.py output_plot
    ```
- For more details on the scenarios and vehicle parameters refer to the [report_26_10_23]

### `P5_FCD_data_analysis`
**Objective:** Analyze Floating Car Data (FCD) XML and make a dataset for analysis and prediction.
- **Flow:** Based on `P4` creating csv file of FCD from xml files (fcd_op.xml and collisions.xml).
- **Contents:** 
  - `output`: simulation analysis results. (includes fcd and collision XML files)
  - `dataset_fcd_col.csv`: FCD dataset combined with collision data
  - `Simulation Analysis.ipynb`: dataset creation, preprocessing and analysis.
 - **How to run**
cmd to run the simulation
     ```sh
    python param_sim_json.py
    ```
    Can also run `intersec.sumocfg` by adjusting the route file `intersec.rou.xml` if you want to visualize the simulation rather than running the cmd line interface.
- For more details on the scenarios, results and vehicle parameters refer to the [report_2_11_23]

## Usage

Navigate through `P1` to `P5` to understand the progression and integration of the analyses. Each directory is equipped with raw and processed data, offering a holistic view of the study. You can modify the parameters based on the experiments you want to conduct. You can generate as many `dataset_fcd_col.csv` files as you want for your analysis/training.

## Links Referred
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information

[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[report_19_10_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_3-veh_type_param_analysis/report_19_10_23.pdf>
[report_26_10_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_3-veh_type_param_analysis/report_26_10_23.pdf>
[report_2_11_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_3-veh_type_param_analysis/report_2_11_23.pdf>
[SUMO simulator]: <https://eclipse.dev/sumo/>
