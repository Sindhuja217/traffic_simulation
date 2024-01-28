import pandas as pd
import xml.etree.ElementTree as ET
from openpyxl import Workbook

def xml_to_excel(xml_file, excel_file, type):
    # Parse XML file
    #tree = ET.parse(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initialize a list to store your data
    data = []

    # Loop through each child of the root element
    if type == 'collision':
        for collision in root.findall('collision'):
            data.append(collision.attrib)

    if type == 'fcd':
        for timestep in root.findall('.//timestep'):
            time = timestep.attrib['time']
            for vehicle in timestep.findall('vehicle'):
                row_data = vehicle.attrib
                row_data['time'] = time
                data.append(row_data)

    if type == 'lane':
       for edge in root.findall(".//edge"):
        edge_id = edge.attrib['id'] 
        for lane in edge.findall("lane"):
            row_data = lane.attrib
            row_data['edge_id'] = edge_id
            data.append(row_data)
    

    
    # Convert list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file
    df.to_excel(excel_file, index=False)

    print(f"Data has been successfully exported to {excel_file}")

if __name__ == "__main__":
    xml_file_collision = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/collisionOutput.xml"
    excel_file_collision = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/collisionOutput.xlsx"
    xml_to_excel(xml_file_collision, excel_file_collision, 'collision')

    xml_file_fcd = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/fcd_output.xml"
    excel_file_fcd = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/fcd_output.xlsx"
    xml_to_excel(xml_file_fcd, excel_file_fcd, 'fcd')

    xml_file_lane = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/lanechange_output.xml"
    excel_file_lane = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/weeklytask-16-11-23/lane_output.xlsx"
    xml_to_excel(xml_file_lane, excel_file_lane, 'lane')


