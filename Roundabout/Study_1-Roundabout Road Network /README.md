# Traffic Simulation for a Roundabout in SUMO 

## Overview
"Simulation of Urban Mobility" (SUMO) is an advanced, open-source traffic simulation tool designed for microscopic and continuous modeling of complex and extensive network systems. This project focuses on the creation and simulation of a roundabout traffic network in SUMO, showcasing its capabilities in accurately simulating traffic management scenarios.

## Project Structure
This project includes the following files, essential for the roundabout traffic simulation:
- `roundabout.net.xml`: This file contains the network design of the roundabout, including lane configurations, traffic signals, and other network attributes.
- `roundabout.rou.xml`: This file defines the traffic demand, specifying various vehicle types and their routes within the network.
- `roundabout.sumocfg`: The configuration file for running the simulation in SUMO, linking the network and route files and setting key simulation parameters.

## Scenarios
The project simulates realistic urban traffic conditions around a roundabout. Utilizing Netedit, a component of SUMO, the roundabout network includes multiple entry and exit points with authentic lane configurations.

## Methodology

### Network Design
- **Tool Used**: Netedit from SUMO suite.
- **Features**: Detailed roundabout design with emphasis on realistic lane configurations and traffic flow directions.

### Traffic Demand
- **Objective**: Simulating real-world peak and off-peak traffic conditions.
- **Vehicles**: Diverse traffic patterns with cars, buses, trucks, etc., to reflect a real traffic environment.

### Simulation Parameters
- **Environment**: SUMO.
- **Settings**: Time steps, vehicle speeds, routing algorithms, etc., for an accurate traffic behavior representation.

## Running the Simulation
To run the simulation:
1. Install SUMO from [SUMO's official website](https://sumo.dlr.de/docs/Downloads.php).
2. Clone this repository and navigate to the project directory.
3. Run SUMO with the configuration file:
   ```bash
   sumo -c roundabout.sumocfg

## Resources and References
- **SUMO Documentation**: [Link to SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- **SUMO Vehicles and Routes**: Comprehensive details on defining vehicles, vehicle types, and routes. [Link to Vehicles and Routes Documentation](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html)
- **Netedit**: A guide to using Netedit for network creation. [Link to Netedit Documentation](https://sumo.dlr.de/docs/Netedit/index.html)
- **SUMO Usage**: Instructions on how to use SUMO for traffic simulations. [Link to SUMO Usage Documentation](https://sumo.dlr.de/docs/sumo.html)

