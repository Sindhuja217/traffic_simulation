# Driver Type Classification Unsupervised

## Driver Type Classification - Unsupervised

### Overview
The report details the process of classifying 1,200 vehicles over a 1,000-second simulation into distinct types using unsupervised learning methods. The simulation generated 400,000 Floating Car Data (FCD) points with 27 attributes, posing challenges for clustering due to potential grouping of different vehicle types.

### Data Pre-processing
- **Aggregation Strategy**: Grouping data by vehicle ID and type, focusing on key features like position, angle, speed, acceleration, and lane information.
- **Dataframe Consolidation**: Combining mean, variance, and standard deviation values into a single dataframe to represent statistical features for each vehicle.

### Unsupervised Learning Models
1. **KMeans Clustering**: Partition-based clustering algorithm.
2. **Hierarchical Clustering**: Tree-based method building clusters hierarchically.

### Dimensionality Reduction Techniques
1. **PCA (Principal Component Analysis)**: Linear technique for orthogonal transformations.
2. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**: Non-linear method focusing on preserving local data structure.
3. **Autoencoder**: Neural network-based technique for encoding and decoding data.

### Approach
- **Data Transformation**: Using PCA, t-SNE, and Autoencoder for dimensionality reduction.
- **Clustering Models**: Applying KMeans and Hierarchical Clustering on transformed data.
- **Clustering Analysis**: Assessing the results of each combination of dimensionality reduction and clustering method.

### Results
- **t-SNE with KMeans Clustering**: Silhouette Score of 0.5707585 suggests moderate cluster definition.
- **Hierarchical Clustering on t-SNE**: Silhouette Score of 0.57686466 indicates reasonably defined clusters.
- **Autoencoders with KMeans**: Silhouette Score of 0.5637805 suggests moderate clustering structure.
- **Hierarchical Clustering on Autoencoded Data**: Silhouette Score of 0.25643113 indicates moderate clustering structure.
- **PCA with KMeans Clustering**: Silhouette Score of 0.482 suggests reasonable cluster definition.
- **Hierarchical Clustering on PCA Data**: Silhouette Score of 0.44 indicates moderate clustering structure.

### Analysis
- **Data Distribution**: Notable differences in data point distribution across clustering methods compared to original data.
- **Clustering Efficacy**: Varying success in defining clusters based on dimensionality reduction and clustering techniques.
- **Challenges**: Discrepancies in clustering results suggest challenges in capturing the inherent grouping of vehicle types accurately.

---

## For more details and better understanding,please refer to report [report_16-11-2023](https://github.com/CL2-UWaterloo/ece699-traffic-simulation/blob/main/HighwayScenario/Study_8-Driver_Type_Classification_Unsupervised/report_16-11-2023.pdf)

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
