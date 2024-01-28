import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import statistics
import math
import re
from collections import Counter
import numpy as np
import sys
import os

file_name = sys.argv[1]

parameter_folder = os.path.join(f"{file_name}")
os.makedirs(parameter_folder, exist_ok=True)

with open('simulation_output.json', "r") as json_file:
    param_sim = json.load(json_file)

total_collisions = {}

for runs, simulations in param_sim.items():
    total_collisions[runs] = simulations['total collisions']

max_avg_param_val = max(total_collisions, key=total_collisions.get)
print(max_avg_param_val)
times = []
lanes = []
types = []
collider_speeds = []
victim_speeds = []
positions= []
collider = []
victim = []

for collision in param_sim[max_avg_param_val]['collisions']:
    times.append(collision['time'])
    lanes.append(collision['lane'])
    types.append(collision['type'])
    positions.append(collision['pos'])
    collider_speeds.append(collision['colliderSpeed'])
    victim_speeds.append(collision['victimSpeed'])
    collider.append(collision['colliderType'])
    victim.append(collision['victimType'])

# heat map       
data_main = pd.DataFrame({
    'Time': times,
    'Collider_Speed': collider_speeds,
    'pos': positions,
    'Victim_Speed': victim_speeds
})

correlation_matrix = data_main.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(parameter_folder,f"correlation_heatmap.png"))

# histograms for time of collision
plt.figure(figsize=(10, 6))
sns.histplot(times, bins=20, color='blue')
plt.title(f'Histogram of Collision Times for simulation number {max_avg_param_val}')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.savefig(os.path.join(parameter_folder,f"collision_times_histogram.png"))

# bar chart for lane of collision
plt.figure(figsize=(10, 6))
sns.countplot(lanes, color='green')
plt.title(f'Bar Chart of Collision Lanes for simulation number {max_avg_param_val}')
plt.xlabel('Lane')
plt.ylabel('Count')
plt.savefig(os.path.join(parameter_folder,f"collision_lanes_barchart.png"))

# colidertype and victimtype
data1 = pd.DataFrame({'Type': ['Collider'] * len(collider) + ['Victim'] * len(victim),
                     'Lane of Collision': collider + victim})

plt.figure(figsize=(12, 6))

# side-by-side bar plot
sns.countplot(data=data1, x='Lane of Collision', hue='Type', palette='Set2')
plt.title('Bar Chart of Lane of Collision')
plt.xlabel('Vehicle Types')
plt.ylabel('Count')
plt.legend(title='Data Source', labels=['Collider', 'Victim'])
plt.savefig(os.path.join(parameter_folder,f"collider_victim_type_bar.png"))

# scatter plot for collider and victim speeds
plt.figure(figsize=(10, 6))
plt.scatter(collider_speeds, victim_speeds, color='red')
plt.title(f'Scatter Plot of Collider and Victim Speeds for simulation number {max_avg_param_val}')
plt.xlabel('Collider Speed')
plt.ylabel('Victim Speed')
plt.savefig(os.path.join(parameter_folder,f"collider_victim_speed_scatter.png"))
