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

    if type == 'fcd':
        for timestep in root.findall('.//timestep'):
            time = timestep.attrib['time']
            for vehicle in timestep.findall('vehicle'):
                row_data = vehicle.attrib
                row_data['time'] = time
                data.append(row_data)

    # Convert list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Write DataFrame to Excel file
    df.to_excel(excel_file, index=False)

    print(f"Data has been successfully exported to {excel_file}")

if __name__ == "__main__":
    xml_file_fcd = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-5thnov/fcd_output.xml"
    excel_file_fcd = "/Users/sindhujach/Desktop/ECE_699/Traffic_simulation/Weeklytask-5thnov/fcd_output.xlsx"
    xml_to_excel(xml_file_fcd, excel_file_fcd, 'fcd')