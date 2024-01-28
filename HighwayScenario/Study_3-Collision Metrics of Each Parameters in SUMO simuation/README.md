# Collision Metrics of Each Parameters in SUMO simuation


## Scenarios

## Scenario 1: Different Type of Collisions with EIDM
Study of rear-end collisions in highway simulation using EIDM, focusing on isolating specific parameters like 'tau', 'collisionMinGapFactor', and 'sigmaerror'.

### Results and Key Observations
- **CollisionMinGapFactor**: Minimum gap between vehicles with observations on collision rate, emergency braking, and stops.
- **SigmaError**: Impact of driver behavior or error modeling on collisions.
- **Tau**: Driver reaction time's influence on collision rates.

### Comparative Analysis
- Smaller minimum gaps and higher sigma errors increase collisions.
- Larger tau values result in safer driving behaviors.

## Scenario 2: Varying Parameters with Constant Tau
In-depth analysis of collision frequency by altering parameters while keeping "tau" constant.

### Car-Following Model Parameters
1. **Sigma Error**: Relationship between sigma and collision rates.
2. **CollisionMinGapFactor**: Impact on collisions with changing factors.
3. **Decel & Emergency Decel**: Influence of deceleration on collisions.
4. **Sigma gap**: Collision rates with varying sigma gap values.

### Lane-change Model Parameters
Investigation of assertive, cooperative, impatient, pushy, and speed gain behaviors on collision rates.

### Junction Model Parameters
Analysis of 'jmIgnoreJunctionFoeProb' and 'jmTimegapMinor' on collision rates.

### Comparative Analysis
- Various parameters' influence on collision rates and driver behaviors.
- Junction-related incidents' impact.

## Scenario 3: Comparative Analysis of Collision Incidents
Study involving Default and Krauss vehicle types, keeping one constant while varying the other.

### Experiment Analyses
1. **Krauss as Constant, Default Type Changed**: Observations on collision rates, emergency measures, and total collisions.
2. **Default as Constant, Krauss Type Changed**: Fluctuations in collision rates and emergency measures.

### Overall Analysis
- The impact of varying vehicle types on collisions and safety measures.

## For more details and better understanding,please refer to report [report_12-10-2023]

## Links reffered
- [SUMO] - SUMO Documentation
- [SUMO Vehicles and Routes] - Definition of Vehicles, Vehicle Types, and Routes and all parameters related information
- [Netedit] - SUMO network edit file
- [SUMO usage] - Usage discription of the simulator


[SUMO]: <https://sumo.dlr.de/docs/index.html>
[SUMO Vehicles and Routes]: <https://sumo.dlr.de/docs/Definition_of_Vehicles%2C_Vehicle_Types%2C_and_Routes.html#junction_model_parameters>
[Netedit]: <https://sumo.dlr.de/docs/Netedit/>
[SUMO usage]: <https://sumo.dlr.de/docs/sumo.html>
[xml2csv]: <https://sumo.dlr.de/docs/Tools/Xml.html>
[Full output xml]: <https://sumo.dlr.de/docs/Simulation/Output/FullOutput.html>


