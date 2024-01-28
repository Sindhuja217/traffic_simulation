#!/bin/bash

export parameter_name="tau" && export param_val="[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.5,1.0]" && python param_sim_json.py
sleep 10
export parameter_name="minGap" && export param_val="[1.5,2,2.5,3,3.5]" && python param_sim_json.py
sleep 10
export parameter_name="sigmaerror" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python param_sim_json.py
sleep 10
export parameter_name="impatience" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python param_sim_json.py
sleep 10
export parameter_name="accel" && export param_val="[0.5,1,2,3,4,5,7,9,10,20]" && python param_sim_json.py
sleep 10
export parameter_name="jmSigmaMinor" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python param_sim_json.py
sleep 10
export parameter_name="tpreview" && export param_val="[4,3,2.5,2,1.5,1]" && python param_sim_json.py
sleep 10
export parameter_name="lcCooperative" && export param_val="[1.0, 0.8, 0.6, 0.4, 0.2, -1]" && python param_sim_json.py
sleep 10
export parameter_name="lcSpeedGain" && export param_val="[0.5, 1.0, 1.5, 2.0, 2.5, 5.0]" && python param_sim_json.py
sleep 10
export parameter_name="lcSigma" && export param_val="[0.0, 0.1, 0.2, 0.3, 0.4, 0.5]" && python param_sim_json.py
sleep 10
export parameter_name="lcPushy" && export param_val="[0.1, 0.3, 0.5, 0.7, 0.9, 1.0]" && python param_sim_json.py

# parameter_name="jmIgnoreFoeProb" by keeping "jmIgnoreFoeSpeed" constant  20 m/s checked it separately on cmd line
# parameter_name="decel" by keeping "emergencyDecel" constant "decel+1" checked it separately on cmd line
# parameter_name="jmDriveAfterRedTime" by keeping "jmDriveRedSpeed" constant  50 m/s check it separately on cmd line
# for more commands do check the run_param_sim.sh file

