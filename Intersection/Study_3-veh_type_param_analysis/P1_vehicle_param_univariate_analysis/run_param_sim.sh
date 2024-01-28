#!/bin/bash

export parameter_name="impatience" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python param_sim_json.py

export parameter_name="jmIgnoreFoeProb" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python param_sim_json.py

export parameter_name="tau" && export param_val="[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.5,1.0]" && python param_sim_json.py

export parameter_name="jmDriveRedSpeed" && export param_val="[50.0, 45.0, 40.0, 35.0, 30.0, 25.0]" && python param_sim_json.py 

export parameter_name="jmIgnoreFoeSpeed" && export param_val="[0.0, 10.0, 20.0, 30.0, 40.0, 60.0]" && python param_sim_json.py 

export parameter_name="speedFactor" && export param_val="[normc(0.8,0.1,0.2,1.5);normc(0.85,0.15,0.2,1.5);normc(1.0,0.15,0.2,1.5);normc(1.15,0.15,0.2,1.5);normc(1.2,0.2,0.2,1.5);normc(1.3,0.2,0.2,1.5)]" && python param_sim_json.py

export parameter_name="emergencyDecel" && export param_val="[5,6,7,8,9,10,15,30,50]" && python param_sim_json.py

# export parameter_name="decel" && export param_val="[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]" && python param_sim_json.py

export parameter_name="accel" && export param_val="[0.5,1,2,3,4,5,7,9,10,20]" && python param_sim_json.py

export parameter_name="sigmaerror" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]" && python param_sim_json.py

export parameter_name="jerkmax" && export param_val="[0.5,1,3,4,6,7,9,10]" && python param_sim_json.py

export parameter_name="minGap" && export param_val="[1.5,2,2.5,3,3.5]" && python param_sim_json.py

export parameter_name="tpreview" && export param_val="[4,3,2,1.5,1]" && python param_sim_json.py

export parameter_name="jmSigmaMinor" && export param_val="[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]" && python param_sim_json.py

export parameter_name="jmDriveAfterRedTime" && export param_val="[-1,0,1,2,4,5,6,8,9,10]" && python param_sim_json.py

export parameter_name="jmTimegapMinor" && export param_val="[1.5, 1.0, 0.8, 0.6, 0.4, 0.2]" && python param_sim_json.py

export parameter_name="lcCooperative" && export param_val="[1.0, 0.8, 0.6, 0.4, 0.2, -1]" && python param_sim_json.py

export parameter_name="lcSpeedGain" && export param_val="[0.5, 1.0, 1.5, 2.0, 2.5, 5.0]" && python param_sim_json.py

export parameter_name="lcPushy" && export param_val="[0.1, 0.3, 0.5, 0.7, 0.9, 1.0]" && python param_sim_json.py

export parameter_name="lcImpatience" && export param_val="[-1.0, -0.5, 0.0, 0.5, 1.0]" && python param_sim_json.py

export parameter_name="lcAssertive" && export param_val="[0.5, 1.0, 1.5, 2.0, 2.5, 3.0]" && python param_sim_json.py

export parameter_name="lcSigma" && export param_val="[0.0, 0.1, 0.2, 0.3, 0.4, 0.5]" && python param_sim_json.py


