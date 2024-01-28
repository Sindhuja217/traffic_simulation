# Study 4 - Driver Type Classification (Supervised and Unsupervised)
This repository hosts datasets, analysis notebooks, and simulation data central to a study on driver type classification and clustering. The project is methodically organized into three principal parts: `simulation_dataset`, `P1-driver_type_supervised`, and `P2-driver_type_unsupervised`, each focusing on a distinct stage of the analysis.

## Directory Structure and Analysis Flow

### `simulation_dataset`
**Objective:** To generate and collect simulation data that forms the base for further analysis.
- **Contents:** 
  - Jupyter notebooks for data preparation (`Dataset for classification.ipynb`).
  - CSV datasets (`dataset_fcd_col.csv`, `output_collision.csv`, `output_emmision.csv`, `output_fcd.csv`).
  - SUMO simulation configuration files (`intersec.net.xml`, `intersec.rou.xml`, `intersec.sumocfg`).
  - Log and JSON output files (`simulation_main.log`, `simulation_output.json`).
  - `param_sim_json.py` for simulation parameters.
  - `output` subdirectory with XML files from the simulations (`collisions.xml`, `em_op.xml`, `fcd_op.xml`, etc.).
- **Usage:** Execute the simulations and use the generated data for subsequent analysis steps. `dataset_fcd_col.csv` is the dataset used for classification and clustering. 
- **How to run:**
    cmd to run the simulation
     ```sh
    python param_sim_json.py
    ```
    Then execute all cells of `Dataset for classification.ipynb`
    Can also run `intersec.sumocfg` by adjusting the route file `intersec.rou.xml` if you want to visualize the simulation rather than running the cmd line interface.
- For more details on the scenarios, and results refer to the [report_9_11_23]

### `P1-driver_type_supervised`
**Objective:** Conduct supervised classification of driver types using the prepared dataset.
- **Flow:** Utilizes data from `simulation_dataset`.
- **Contents:**
  - Shared dataset file: `dataset_fcd_col.csv`.
  - Jupyter notebooks implementing different supervised classification models (`DNN_TYPE_CLASSIFICATION.ipynb`, `driver-type-classification-label-encoding.ipynb`, `driver-type-classification-one-hot.ipynb`).
- **Usage:** Execute the notebooks to carry out supervised classification analysis. Change the location of `dataset_fcd_col.csv` in pynb file as it was run on Google Collab.
- For more details on the models, and results refer to the [report_9_11_23]

### `P2-driver_type_unsupervised`
**Objective:** Apply unsupervised learning techniques for driver type clustering.
- **Flow:** Continues the analysis using the dataset from `simulation_dataset`.
- **Contents:**
  - Shared dataset file: `dataset_fcd_col.csv`.
  - Jupyter notebook for clustering analysis (`driver-type-clustering.ipynb`). Change the location of `dataset_fcd_col.csv` in pynb file as it was run on Kaggle.
- **Usage:** Run the notebook to perform unsupervised learning methods on the driver type data.
- For more details on the models, and results refer to the [report_16_11_23]

## General Instructions

- Ensure that all necessary software and libraries (like Python, Jupyter, and tensorflow) are installed.
- Begin with the `simulation_dataset` to generate and prepare your data.
- Progress to `P1-driver_type_supervised` for detailed supervised classification.
- Conclude with `P2-driver_type_unsupervised` for insights via unsupervised methods.

[report_9_11_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_4-driver_type_classification/report_9_11_23.pdf>
[report_16_11_23]: <https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/Intersection/Study_4-driver_type_classification/report_16_11_23.pdf>
