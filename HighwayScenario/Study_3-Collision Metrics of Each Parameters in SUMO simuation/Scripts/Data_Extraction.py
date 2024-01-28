#!/usr/bin/env python

import os
import sys
import optparse
import pandas as pd
import xml.etree.ElementTree as ET

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci

def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

# Function to parse XML and extract collision data
def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    collision_data = []

    for collision in root.findall('.//collision'):
        data = {
            'Time': collision.get('time'),
            'Type': collision.get('type'),
            'Lane': collision.get('lane'),
            'Position': collision.get('pos'),
            'Collider': collision.get('collider'),
            'Victim': collision.get('victim'),
            'ColliderType': collision.get('colliderType'),
            'VictimType': collision.get('victimType'),
            'ColliderSpeed': collision.get('colliderSpeed'),
            'VictimSpeed': collision.get('victimSpeed')
        }
        collision_data.append(data)

    return collision_data

def run():
    step = 0
    collision_data = []

    while step < 500:  # Increase the number of simulation steps for better data
        traci.simulationStep()
        step += 1

    # Get collision data
    collisions = traci.simulation.getCollisions()
    if collisions is not None:
        collision_data.append(collisions)

    return collision_data

import xml.etree.ElementTree as ET

# def update_xml_parameters(xml_file, parameter_value):
#     # Parse the XML file
#     tree = ET.parse(xml_file)
#     root = tree.getroot()

#     # Locate and modify the tau value
#     for vType in root.iter('vType'):
#         if vType.get('id') == 'DEFAULT_VEHTYPE':
#             vType.set('collisionMinGapFactor', str(parameter_value))

#     # Save the modified XML
#     modified_xml_file = f"modified_{parameter_value}.rou.xml"
#     tree.write(modified_xml_file)

#     return modified_xml_file



if __name__ == "__main__":
    options = get_options()

    # Check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # Specify the range of parameter values
    parameter_values = [10,20,30,40,50,60,70,80,90,100]  # Add your desired values

    for value in parameter_values:
        # Update the XML file with the parameter value
        # modified_xml_file = update_xml_parameters("Highway.rou.xml", value)

            # Start SUMO with the modified XML file
            # traci.start([sumoBinary, "-c", "Highway_sumoconfig.sumocfg", "--collision-output", "Collisiondata_tau.xml", "-r", modified_xml_file])
            traci.start([sumoBinary, "-c", "Highway_sumoconfig.sumocfg", "--collision-output", "Collisiondata_tau.xml","--statistic-output","Statisticdata_tau.xml","--max-num-vehicles",str(value),"--step-length","1","--collision.action","remove","--collision.stoptime","0.30","--random"])

            # Run the simulation and get collision data
            collision_data = run()

            # Close SUMO
            traci.close()

            # Generate a unique Excel file name based on the parameter value
            excel_file = f'C:/Users/saiko/OneDrive/Desktop/699/Task-3/DifferentFinal_1.xlsx'

            # Parse XML and extract collision data
            collision_data = parse_xml("Collisiondata_tau.xml")

            # Create a DataFrame from the collision data
            df = pd.DataFrame(collision_data)

            # Write the DataFrame to an Excel file
            excel_writer = pd.ExcelWriter(excel_file, engine='openpyxl', mode='a', if_sheet_exists="replace")
            sheet_name = str(value)
            # Write the DataFrame to an Excel sheet with the specified sheet name
            df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

            # Save and close the Excel file
            excel_writer._save()
            excel_writer.close()
            
            if 'ColliderType' in df.columns:
        # Calculate type_counts
                type_counts = df['ColliderType'].value_counts()
                
                # Check if type_counts is empty (no records in 'Type' column)
                if type_counts.empty:
                    # If it's empty, create a DataFrame with 'Collision_Count' and 'Junction_Count' as 0
                    df_types = pd.DataFrame({'aggressive': [0], 'tailgater': [0],'passive':[0],'speeder':[0]})
                else:
                    # If it's not empty, create a DataFrame from type_counts
                    df_types = pd.DataFrame(type_counts).T
                    # Reset the index for df_types
                    df_types.reset_index(drop=True, inplace=True)
                    # Rename the columns for better clarity
                    df_types.rename(columns={"collision": "Collision_Count", "junction": "Junction_Count"}, inplace=True)
            else:
                # If 'Type' column doesn't exist, create a DataFrame with 'Collision_Count' and 'Junction_Count' as 0
                df_types = pd.DataFrame({'aggressive': [0], 'tailgater': [0],'passive':[0],'speeder':[0]})

            print('Conversion completed. Excel file saved as', excel_file)

                


            import pandas as pd
            import xml.etree.ElementTree as ET

            # Function to parse XML and extract statistics data
            def parse_statistics_xml(xml_file):
                tree = ET.parse(xml_file)
                root = tree.getroot()

                statistics_data1 = []
                statistics_data2 = []

                for stat in root.findall('.//safety'):
                    data1 = {
                        'Collsions': stat.get('collisions'),
                        'emergencyBraking': stat.get('emergencyBraking'),
                        'emergencyStops': stat.get('emergencyStops'),

                    }
                    statistics_data1.append(data1)
                for stat in root.findall('.//vehicles'):
                    data2 = {
                        'loaded': stat.get('loaded'),
                        'inserted': stat.get('inserted'),
                        'running': stat.get('running'),

                    }
                    statistics_data2.append(data2)
                # Convert the lists of dictionaries into DataFrames
                df1 = pd.DataFrame(statistics_data1)
                df2 = pd.DataFrame(statistics_data2)

                # Reset the index for both DataFrames
                df1.reset_index(drop=True, inplace=True)
                df2.reset_index(drop=True, inplace=True)

                # Concatenate the DataFrames horizontally
                merged_df = pd.concat([df1, df2], axis=1)
                return merged_df

            # XML input file
            xml_file = "Statisticdata_tau.xml"

            # Parse XML and extract collision data
            stats_data = parse_statistics_xml(xml_file)

            # Create a DataFrame from the collision data
            df_stats = pd.DataFrame(stats_data)





            df_stats['Collsions'] = pd.to_numeric(df_stats['Collsions'], errors='coerce')
            df_stats['loaded'] = pd.to_numeric(df_stats['loaded'], errors='coerce')

            # Calculate rates while handling potential missing or non-numeric values
            rate_of_collisions_time = df_stats['Collsions'] / 500
            rate_of_collisions_time = rate_of_collisions_time.values[0]
            rate_of_collisions_inserted = df_stats['Collsions'] / df_stats['loaded']
            rate_of_collisions_inserted = rate_of_collisions_inserted.values[0]
            df_values = pd.DataFrame(columns=['Value','rate_of_collisions_time','rate_of_collisions_inserted'])

            # At each run, insert a new value
            # Replace this with your actual new value
            df_values = df_values._append({'Value': value,'rate_of_collisions_time':rate_of_collisions_time,'rate_of_collisions_inserted':rate_of_collisions_inserted}, ignore_index=True)

            final_merged_df = pd.concat([df_values,df_stats, df_types], axis=1)

            # Write the DataFrame to an Excel file
            excel_writer_metrics = pd.ExcelWriter(excel_file, engine='openpyxl', mode='a',if_sheet_exists="overlay")

                # Write the DataFrame to an Excel sheet with the specified sheet name
            final_merged_df.to_excel(excel_writer_metrics,index=False,sheet_name="Sheet1",header=True,startrow=excel_writer_metrics.sheets['Sheet1'].max_row)

                # Save and close the Excel file
            excel_writer_metrics._save()
            excel_writer_metrics.close()
            print('Conversion completed. CSV file saved as', excel_writer_metrics)
            

    print("Simulations completed.")
