import xml.etree.ElementTree as ET
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

ego_vehicle_id = 'ego_car'
pd.options.mode.chained_assignment = None 

# Function to parse the FCD XML and extract ego vehicle data
def parse_fcd_data(fcd_file, ego_vehicle_id):
    tree = ET.parse(fcd_file)
    root = tree.getroot()

    fcd_data = []
    for timestep in root.findall('timestep'):
        time = float(timestep.get('time'))
        for vehicle in timestep.findall('vehicle'):
            if vehicle.get('id') == ego_vehicle_id:
                fcd_data.append({
                    'time': float(time),
                    'id': vehicle.get('id'),
                    'speed': float(vehicle.get('speed')),
                    'x': float(vehicle.get('x')),
                    'y': float(vehicle.get('y')),
                    'lane': vehicle.get('lane'),
                    'angle': float(vehicle.get('angle')),
                    'type': vehicle.get('type'),
                    'pos': float(vehicle.get('pos')),
                    'slope': float(vehicle.get('slope'))
                })
    return pd.DataFrame(fcd_data)

def parse_fcd_data_1(fcd_file):
    tree = ET.parse(fcd_file)
    root = tree.getroot()

    fcd_data = []
    for timestep in root.findall('timestep'):
        time = float(timestep.get('time'))
        for vehicle in timestep.findall('vehicle'):
            # No filtering, we add data for all vehicles now
            fcd_data.append({
                'time': float(time),
                'id': vehicle.get('id'),  # Changed 'id' to 'vehicle_id' for clarity
                'speed': float(vehicle.get('speed')),
                'x': float(vehicle.get('x')),
                'y': float(vehicle.get('y')),
                'lane': vehicle.get('lane'),
                'angle': float(vehicle.get('angle')),
                'type': vehicle.get('type'),
                'pos': float(vehicle.get('pos')),  # Changed 'pos' to 'position' for clarity
                'slope': float(vehicle.get('slope'))
            })
    return pd.DataFrame(fcd_data)

# Function to parse collision data XML
def parse_collision_data(collision_file):
    tree = ET.parse(collision_file)
    root = tree.getroot()

    collision_data = []
    for collision in root.findall('collision'):
        time = float(collision.get('time'))
        collider = collision.get('collider')
        victim = collision.get('victim')
        collision_data.append({'CollisionTime': time, 'Collider': collider, 'Victim': victim})

    return pd.DataFrame(collision_data)

# Merge FCD and collision data
def merge_data(fcd_df, collision_df):
    # Add a column for collision flag, initialized to 0 (no collision)
    fcd_df['Collision'] = 0

    # Check for collisions at each time step
    for index, row in fcd_df.iterrows():
        if any((collision_df['CollisionTime'] == row['time']) & ((collision_df['Collider'] == row['id']) | (collision_df['Victim'] == row['id']))):
            fcd_df.at[index, 'Collision'] = 1

    return fcd_df

# File paths
for i in range(5):
    fcd_file_path = f'/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-7-12-23/fcd_output_run_{i}.xml'
    collision_file_path = f'/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-7-12-23/collision_output_run_{i}.xml'

    # Parsing XML files
    fcd_df = parse_fcd_data(fcd_file_path, 'ego_car')
    fcd_df_1 = parse_fcd_data_1(fcd_file_path)
    collision_df = parse_collision_data(collision_file_path)
    collision_df.to_excel(f'collision_data_{i}.xlsx', index=False)
    print(f"Data saved to collision_data_{i}.xlsx")

    # Merging the data
    merged_df = merge_data(fcd_df, collision_df)

    features = merged_df[['speed', 'x', 'y']]
    target = merged_df['Collision']

    df = pd.DataFrame(merged_df, columns=['time', 'id', 'speed', 'x', 'y', 'lane', 'angle', 'type', 'pos', 'slope', 'Collision'])

    # Save DataFrame to CSV
     
    df.to_excel(f'ego_vehicle_data_{i}.xlsx', index=False)
    print(f"Data saved to ego_vehicle_data_{i}.xlsx")

    df_sorted = df.sort_values(by='time', ascending = True)
    df_sorted.reset_index(drop=True, inplace=True)
    df_sorted.to_excel(f'fcd_data_sorted_{i}.xlsx', index=False)
    print(f"Data saved to fcd_data_sorted_{i}.xlsx")

    # Sort the DataFrame by 'time' to ensure chronological order
    fcd_df_1.sort_values(by='time', inplace=True)
    fcd_df_1.reset_index(drop=True, inplace=True)
    fcd_df_1['acceleration'] = fcd_df_1.groupby('id')['speed'].diff() / fcd_df_1.groupby('id')['time'].diff()
    fcd_df_1['acceleration'] = fcd_df_1['acceleration'].fillna(0)

    # Assuming df is your DataFrame
    #df_sorted['acceleration'][0] = 0.0
    #print('df_sorted', df_sorted)

    # Group the DataFrame by 'time' and 'lane'
    grouped = fcd_df_1.groupby(['time', 'lane'])

    fcd_df_1['nearest_vehicle_id'] = None
    fcd_df_1['least_distance'] = np.inf
    fcd_df_1['relative_speed'] = np.nan

    # Calculate the nearest vehicle and least distance
    for time in fcd_df_1['time'].unique():
        current_time_slice = fcd_df_1[fcd_df_1['time'] == time]
        for index, row in current_time_slice.iterrows():
            # Calculate distances from the current vehicle to all others at the same time step
            distances = current_time_slice.apply(
                lambda r: np.hypot(r['x'] - row['x'], r['y'] - row['y']) if r['id'] != row['id'] else np.inf, axis=1)
            # Get the index of the minimum distance
            min_dist_index = distances.idxmin()
            # Assign the nearest vehicle ID and the least distance
            fcd_df_1.at[index, 'nearest_vehicle_id'] = fcd_df_1.at[min_dist_index, 'id']
            fcd_df_1.at[index, 'least_distance'] = distances.min()
            # Calculate relative speed
            fcd_df_1.at[index, 'relative_speed'] = abs(row['speed'] - fcd_df_1.at[min_dist_index, 'speed'])

    # Save the DataFrame with the new calculations
    # Save the enhanced DataFrame with new calculations to unique Excel file
    fcd_df_1.to_excel(f'enhanced_fcd_data_{i}.xlsx', index=False)
    print(f"Data saved to enhanced_fcd_data_{i}.xlsx")

    ego_car_data = fcd_df_1.loc[fcd_df_1['id'] == ego_vehicle_id]

    # Save ego vehicle data to unique Excel file
    ego_car_data.to_excel(f'ego_vehicle_data_only_{i}.xlsx', index=False)
    print(f"Data saved to ego_vehicle_data_only_{i}.xlsx")

    ego_car_data_unique = ego_car_data.drop_duplicates()
    # Consider if you need a unique file for each run or a combined file
    ego_car_data_unique.to_excel('unique_ego_vehicle_data.xlsx', index=False)
    print("Data saved to unique_ego_vehicle_data.xlsx")