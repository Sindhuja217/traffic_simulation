import xml.etree.ElementTree as ET
import pandas as pd

# Parse the collision data XML file
collision_tree = ET.parse("/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-26-10-23/collisionOutput.xml")
collision_root = collision_tree.getroot()

# Parse the FCD data XML file
fcd_tree = ET.parse("/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-26-10-23/fcd_output.xml")
fcd_root = fcd_tree.getroot()

# Parse the statistic data XML file
stat_tree = ET.parse("/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-26-10-23/statistic_output2.xml")
stat_root = stat_tree.getroot()

# Create a list to store extracted data
merged_data = []

# Extract data from collision output
for collision in collision_root.findall('collision'):
    time = float(collision.get('time'))
    collider = collision.get('collider')

    # Search for matching data in FCD output based on time
    for timestep in fcd_root.findall('timestep'):
        if float(timestep.get('time')) == time - 1:
            for vehicle in timestep.findall('vehicle'):
                if vehicle.get('id') == collider:
                    x = float(vehicle.get('x'))
                    y = float(vehicle.get('y'))
                    # Add more attributes as needed
                    merged_data.append({'time': time, 'collider': collider, 'x': x, 'y': y})

# Extract safety-related data from statistic output
safety_data = stat_root.find('safety')
collision_count = int(safety_data.get('collisions'))
emergency_stops = int(safety_data.get('emergencyStops'))
emergency_braking = int(safety_data.get('emergencyBraking'))

# Create a pandas DataFrame from the merged data
merged_df = pd.DataFrame(merged_data)

# Add safety-related data to the DataFrame
merged_df['collision_count'] = collision_count
merged_df['emergency_stops'] = emergency_stops
merged_df['emergency_braking'] = emergency_braking

# Write the merged data to an Excel file
merged_df.to_excel("merged_data.xlsx", index=False)