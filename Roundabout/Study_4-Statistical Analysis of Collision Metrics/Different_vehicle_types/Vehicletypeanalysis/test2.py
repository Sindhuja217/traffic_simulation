import xml.etree.ElementTree as ET
from openpyxl import Workbook
from collections import defaultdict
import matplotlib.pyplot as plt

# Parse XML
tree = ET.parse('collision_output.xml')
root = tree.getroot()

# Dictionary to store the count of collisions for each vehicle type
collision_count = defaultdict(int)

# Extract data
for collision in root.findall('collision'):
    colliderType = collision.get('colliderType')
    victimType = collision.get('victimType')

    collision_count[colliderType] += 1
    collision_count[victimType] += 1

# Create a new workbook and get the active worksheet
wb = Workbook()
ws = wb.active

# Let's say your XML has a structure like this:
# <data>
#   <entry name="name1" value="value1" />
#   <entry name="name2" value="value2" />
#   ...
# </data>

# Write headers
ws.append(['Time', 'Type', 'Lane', 'Pos', 'Collider', 'Victim', 'ColliderType', 'VictimType', 'ColliderSpeed', 'VictimSpeed'])


# Extract data and write to Excel
for collision in root.findall('collision'):
    time = collision.get('time')
    type = collision.get('type')
    lane = collision.get('lane')
    pos = collision.get('pos')
    collider = collision.get('collider')
    victim = collision.get('victim')
    colliderType = collision.get('colliderType')
    victimType = collision.get('victimType')
    colliderSpeed = collision.get('colliderSpeed')
    victimSpeed = collision.get('victimSpeed')
    ws.append([time, type, lane, pos, collider, victim, colliderType, victimType, colliderSpeed, victimSpeed])

# Save to XLSX
wb.save('collision_output.xlsx')

# Plot the graph
vehicle_types = list(collision_count.keys())
collisions = list(collision_count.values())

plt.figure(figsize=(10, 6))
plt.bar(vehicle_types, collisions, color=['red', 'blue', 'green', 'yellow'])
plt.xlabel('Vehicle Type')
plt.ylabel('Number of Collisions')
plt.title('Number of Collisions per Vehicle Type')
plt.tight_layout()
plt.show()

collider_count = defaultdict(int)
victim_count = defaultdict(int)

# Extract data
for collision in root.findall('collision'):
    colliderType = collision.get('colliderType')
    victimType = collision.get('victimType')

    collider_count[colliderType] += 1
    victim_count[victimType] += 1
# Plot the grouped bar chart
vehicle_types = list(collider_count.keys())

# Define the width of the bars
bar_width = 0.35
index = range(len(vehicle_types))

# Plotting
plt.figure(figsize=(10, 6))
bar1 = plt.bar(index, [collider_count[v] for v in vehicle_types], bar_width, color='red', label='Collider')
bar2 = plt.bar([i+bar_width for i in index], [victim_count[v] for v in vehicle_types], bar_width, color='blue', label='Victim')

# Labeling, title and axes ticking
plt.xlabel('Vehicle Type')
plt.ylabel('Number of Collisions')
plt.title('Number of Collisions per Vehicle Type')
plt.xticks([i+bar_width/2 for i in index], vehicle_types)  # Positioning the vehicle type labels in the middle of the grouped bars
plt.legend()

# Display
plt.tight_layout()
plt.show()