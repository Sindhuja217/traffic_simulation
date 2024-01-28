# Lanelet2 Conversion and Classification Model for SUMO Simulations

## Lanelet2 Conversion
This project focuses on converting SUMO simulation data into the Lanelet2 format, enhancing the precision and utility of traffic simulations for autonomous vehicle research.

### Conversion Process
- **Step 1**: Convert SUMO's XML data to OpenDrive format.
- **Step 2**: Transform OpenDrive data into Lanelet2 format, preserving detailed road network information.

## Methodology
The conversion process employs `netconvert` for initial transformation, followed by custom scripts and tools to ensure accurate Lanelet2 mapping.

### Tools and Techniques
- **CommonRoad Designer**: Utilized for editing and scenario creation in Lanelet2 format.
- **JOSM**: Employed for detailed visualization and further editing of Lanelet2 data.

## Classification Model
Post-conversion, the project implements machine learning models to classify vehicle types based on traffic simulation data.

### Model Implementation
- **Models Used**: Random Forest, Gradient Boosting, and Deep Neural Networks.
- **Objective**: Accurately classify vehicle types to enhance the realism of traffic simulations.

### Key Findings
- **Random Forest Accuracy**: Demonstrated high efficiency in vehicle type classification.
- **Data Complexity Handling**: Advanced modeling techniques were applied for effective feature analysis and classification.

## Future Directions
Exploring more complex deep learning models and ensemble methods to further improve classification accuracy.

## Resources
- [SUMO Documentation](https://sumo.dlr.de/docs/index.html)
- [Lanelet2 Overview](https://www.mrt.kit.edu/z/publ/download/2018/Poggenhans2018Lanelet2.pdf)
- [CommonRoad Designer](https://commonroad.in.tum.de/)
- [JOSM Editor](https://josm.openstreetmap.de/)
