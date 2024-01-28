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
pattern = r"simulation_output_(\w+)\.json"
match = re.search(pattern, file_name)
parameter_name = match.group(1)
parameter_folder = os.path.join("output_plot_50", f"{parameter_name}") # change this to output_plot_30 for 30% ego cars plot directory
os.makedirs(parameter_folder, exist_ok=True)

with open(file_name, "r") as json_file:
    param_sim = json.load(json_file)

total_collisions = {}

for param_val, simulations in param_sim.items():
    total_collisions[param_val] = sum([details['total collisions'] for details in simulations.values()])

max_avg_param_val = max(total_collisions, key=total_collisions.get)

times = []
lanes = []
types = []
collider_speeds = []
victim_speeds = []
positions= []

for simulation_number, simulation_details in param_sim[max_avg_param_val].items():
    for collision in simulation_details['collisions']:
        times.append(collision['time'])
        lanes.append(collision['lane'])
        types.append(collision['type'])
        positions.append(collision['pos'])
        collider_speeds.append(collision['colliderSpeed'])
        victim_speeds.append(collision['victimSpeed'])

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
plt.savefig(os.path.join(parameter_folder,f"correlation_heatmap_{parameter_name}.png"))

# histograms for time of collision
plt.figure(figsize=(10, 6))
sns.histplot(times, bins=20, color='blue')
plt.title(f'Histogram of Collision Times for {parameter_name}' + str(max_avg_param_val))
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.savefig(os.path.join(parameter_folder,f"collision_times_histogram_{parameter_name}.png"))

# bar chart for lane of collision
plt.figure(figsize=(10, 6))
sns.countplot(lanes, color='green')
plt.title(f'Bar Chart of Collision Lanes for {parameter_name}' + str(max_avg_param_val))
plt.xlabel('Lane')
plt.ylabel('Count')
plt.savefig(os.path.join(parameter_folder,f"collision_lanes_barchart_{parameter_name}.png"))

# scatter plot for collider and victim speeds
plt.figure(figsize=(10, 6))
plt.scatter(collider_speeds, victim_speeds, color='red')
plt.title(f'Scatter Plot of Collider and Victim Speeds for {parameter_name}' + str(max_avg_param_val))
plt.xlabel('Collider Speed')
plt.ylabel('Victim Speed')
plt.savefig(os.path.join(parameter_folder,f"collider_victim_speed_scatter_{parameter_name}.png"))

# mean mode analysis
cols_params_avg = []
cols_params_mode = []
cols_params_min = []
cols_params_max = []
cols_params_median = []
embr_params_avg = []
cols_dic = {}
emer_dic = {}
param_ls = [i for i in param_sim.keys()]
for param in param_sim.keys():
    total_cols = []
    total_emergency_brakes = []
    for sim_run,sim_details in param_sim[param].items():
        total_cols.append(sim_details['total collisions'])
        total_emergency_brakes.append(sim_details['emergency brakes'])
    cols_dic[param] = total_cols
    emer_dic[param] = total_emergency_brakes
    cols_params_avg.append(math.ceil(statistics.mean(total_cols)))
    embr_params_avg.append(math.ceil(statistics.mean(total_emergency_brakes)))
    cols_params_mode.append(statistics.mode(total_cols))
    cols_params_min.append(min(total_cols))
    cols_params_max.append(max(total_cols))
    cols_params_median.append(math.ceil(statistics.median(total_cols)))
bar_width = 0.4
bar_positions = np.arange(len(param_ls))

mean_color = 'blue'
mode_color = 'orange'
plt.figure(figsize=(10, 6))
plt.bar(bar_positions - bar_width / 2, cols_params_avg, width=bar_width, label='Mean', color=mean_color)
plt.bar(bar_positions + bar_width / 2, cols_params_mode, width=bar_width, label='Mode', color=mode_color)
plt.plot(bar_positions - bar_width / 2, cols_params_avg, marker='o', markersize=4, color='black', linestyle='None')
plt.plot(bar_positions + bar_width / 2, cols_params_mode, marker='o', markersize=4, color='black', linestyle='None')
plt.title(f'MEAN and MODE ANALYSIS: Total Number of Collisions vs. {parameter_name}')
plt.xlabel(parameter_name)
plt.ylabel('Total Number of Collisions')
plt.grid(True)
plt.legend(fontsize=12)
plt.minorticks_on()
plt.xticks(bar_positions, param_ls)
plt.tight_layout()
plt.savefig(os.path.join(parameter_folder,f"bar_mean_mode_{parameter_name}.png"))

# bar chart for total collisions and emergency brakes
bar_width = 0.35
plt.figure(figsize=(10, 6))
plt.bar(np.arange(len(param_ls)) - bar_width/2, cols_params_avg, bar_width, label='average_total_collisions', color='blue')
plt.bar(np.arange(len(param_ls)) + bar_width/2, embr_params_avg, bar_width, label='average_total_emergency_brakes', color='green')
plt.xlabel(f'{parameter_name}')
plt.ylabel('Count')
plt.title(f'Collision and Emergency Brake Events by {parameter_name}')
plt.xticks(np.arange(len(param_ls)), param_ls)
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(parameter_folder,f"coll_emerbrakes_{parameter_name}.png"))

# box plot
data_values = list(cols_dic.values())
param_labels = list(cols_dic.keys())
plt.figure(figsize=(10, 6))
boxprops = dict(linestyle='-', linewidth=2, color='blue')
flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='red')
medianprops = dict(linestyle='-', linewidth=2, color='green')
plt.boxplot(data_values, labels=param_labels, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops)
plt.xlabel(f'{parameter_name}')
plt.ylabel('Values')
plt.title('Box Plot of Data')
plt.grid(True)
plt.tight_layout()  
plt.savefig(os.path.join(parameter_folder,f"box_plot_collision_{parameter_name}.png"))

# min max median plot
plt.figure(figsize=(10, 6))
plt.plot(param_ls, cols_params_median, marker='o', linestyle='-', label='Median')
plt.plot(param_ls, cols_params_min, marker='o', linestyle='-', label='Minimum')
plt.plot(param_ls, cols_params_max, marker='o', linestyle='-', label='Maximum')
plt.fill_between(param_ls, cols_params_min, cols_params_max, alpha=0.3, label='Range')
plt.title(f'Total Number of Collisions vs. {parameter_name}')
plt.xlabel(parameter_name)
plt.ylabel('Total Number of Collisions')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(parameter_folder,f"min_max_median_{parameter_name}.png"))
