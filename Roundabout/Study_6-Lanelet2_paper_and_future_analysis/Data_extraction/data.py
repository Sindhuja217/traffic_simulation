import xml.etree.ElementTree as ET
import pandas as pd

collision_excel_file  = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-30-10-23/collisionOutput2.xlsx"
fcd_excel_file = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-30-10-23/fcd_output2.xlsx"
lane_excel_file = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-30-10-23/lane_output2.xlsx"

collision_df = pd.read_excel(collision_excel_file)
fcd_df = pd.read_excel(fcd_excel_file)
lane_df = pd.read_excel(lane_excel_file)

net_file_path = '/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Roundabout/new.net.xml'

tree = ET.parse(net_file_path)
root = tree.getroot()

# Extract lane information
lane_data = []
for edge in root.findall('edge'):
    for lane in edge.findall('lane'):
        lane_id = lane.get('id')
        lane_length = float(lane.get('length'))
        lane_data.append({'lane_id': lane_id, 'lane_length': lane_length})

lane_dataframe = pd.DataFrame(lane_data)

fcd_df['lane_id'] = fcd_df['lane'].astype(str)
lane_df['lane_id'] = lane_df['id'].astype(str)
fcd_df['vehicle_id'] = fcd_df['id'].astype(str)

fcd_df = pd.merge(fcd_df, lane_dataframe[['lane_id', 'lane_length']], on='lane_id', how='left')

#print(fcd_df.head())

# Assuming df_collision is your collision data DataFrame
df_collision = collision_df.sort_values(by=['lane', 'time'])
df_collision['time_since_last_collision'] = df_collision.groupby('lane')['time'].diff()

#print(df_collision.head())

# Assuming df_fcd is your FCD data DataFrame
fcd_df['count'] = 1
vehicle_density = fcd_df.groupby(['lane_id', 'time', 'lane_length'])['count'].sum().reset_index()
vehicle_density.to_excel('vehicle_density.xlsx', index = False)


vehicle_density['vehicle_density'] = vehicle_density['count'] / vehicle_density['lane_length']

average_speed = fcd_df.groupby(['lane_id', 'time'])['speed'].mean().reset_index()
average_speed.rename(columns={'speed': 'avg_speed_nearby_vehicles'}, inplace=True)

#speed_variance = fcd_df.groupby(['lane_id', 'time'])['speed'].var().reset_index()
#speed_variance.rename(columns={'speed': 'var_speed_nearby_vehicles'}, inplace=True)
#print(speed_variance)

df_fcd = fcd_df.sort_values(by=['vehicle_id', 'time'])
df_fcd['time'] = pd.to_numeric(df_fcd['time'], errors='coerce')


df_fcd['lane_change'] = df_fcd.groupby('vehicle_id')['lane_id'].shift(0) != df_fcd.groupby('vehicle_id')['lane_id'].shift(-1)
df_fcd['lane_change'] = df_fcd['lane_change'].astype(int) 
df_fcd['lane_id'] = df_fcd['lane_id'].astype(str)
#print(df_fcd)

#df_fcd['lane_id'] = pd.to_numeric(df_fcd['lane_id'], errors='coerce')
df_fcd['time'] = pd.to_numeric(df_fcd['time'], errors='coerce')

#vehicle_density['lane_id'] = pd.to_numeric(vehicle_density['lane_id'], errors='coerce')
vehicle_density['time'] = pd.to_numeric(vehicle_density['time'], errors='coerce')

#average_speed['lane_id'] = pd.to_numeric(average_speed['lane_id'], errors='coerce')
average_speed['time'] = pd.to_numeric(average_speed['time'], errors='coerce')
#print(average_speed)

#speed_variance['lane_id'] = pd.to_numeric(speed_variance['lane_id'], errors='coerce')
#speed_variance['time'] = pd.to_numeric(speed_variance['time'], errors='coerce')


df_fcd['lane_id'] = df_fcd['lane_id'].astype(str)
vehicle_density['lane_id'] = vehicle_density['lane_id'].astype(str)
average_speed['lane_id'] = average_speed['lane_id'].astype(str)
#speed_variance['lane_id'] = speed_variance['lane_id'].astype(str)

features = df_fcd.merge(vehicle_density[['lane_id', 'time', 'vehicle_density']], on=['lane_id', 'time'], how='left')
features = features.merge(average_speed[['lane_id', 'time', 'avg_speed_nearby_vehicles']], on=['lane_id', 'time'], how='left')
#features = features.merge(speed_variance[['lane_id', 'time', 'var_speed_nearby_vehicles']], on=['lane_id', 'time'], how='left')

features = features.drop('vehicle_id', axis = 1)
features = features.drop('slope', axis = 1)
features = features.drop('count', axis = 1)
#features.to_excel('features.xlsx', index = False)

features['collision'] = 0

for index, row in collision_df.iterrows():
    time = row['time']
    collider = row['collider']

    mask = (features['time'] == time - 1) & (features['id'] == collider)

    features.loc[mask, 'collision'] = 1


features.to_excel('features.xlsx', index = False)