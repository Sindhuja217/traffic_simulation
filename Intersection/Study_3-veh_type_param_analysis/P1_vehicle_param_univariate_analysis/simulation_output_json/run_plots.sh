#!/bin/bash

python plots.py json_files_50/simulation_output_accel.json
python plots.py json_files_50/simulation_output_jmIgnoreFoeProb.json
python plots.py json_files_50/simulation_output_lcSigma.json
python plots.py json_files_50/simulation_output_tau.json
python plots.py json_files_50/simulation_output_decel.json 
python plots.py json_files_50/simulation_output_jmSigmaMinor.json
python plots.py json_files_50/simulation_output_lcSpeedGain.json
python plots.py json_files_50/simulation_output_tpreview.json
python plots.py json_files_50/simulation_output_impatience.json
python plots.py json_files_50/simulation_output_lcCooperative.json
python plots.py json_files_50/simulation_output_minGap.json
python plots.py json_files_50/simulation_output_jmDriveAfterRedTime.json
python plots.py json_files_50/simulation_output_lcPushy.json 
python plots.py json_files_50/simulation_output_sigmaerror.json

# change json_files_50 to json_files_30 for 30% ego cars plots