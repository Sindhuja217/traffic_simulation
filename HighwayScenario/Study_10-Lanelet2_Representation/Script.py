import xml.etree.ElementTree as ET

def parse_fcd_data(fcd_file):
    tree = ET.parse(fcd_file)
    root = tree.getroot()
    fcd_data = []
    for timestep in root.findall('timestep'):
        time = timestep.get('time')
        for vehicle in timestep.findall('vehicle'):
            fcd_data.append({
                'time': time,
                'id': vehicle.get('id'),
                'lat': float(vehicle.get('y')),  # Assuming 'y' is latitude
                'lon': float(vehicle.get('x'))   # Assuming 'x' is longitude
            })
    return fcd_data

def parse_lanelet2_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    nodes = {}
    ways = {}
    relations = {}
    node_to_way = {}  # Map node ID to way ID
    way_to_relation = {}  # Map way ID to relation (lanelet) ID

    for element in root:
        if element.tag == 'node':
            node_id = element.get('id')
            lat = float(element.get('lat'))
            lon = float(element.get('lon'))
            nodes[node_id] = {'lat': lat, 'lon': lon}

        elif element.tag == 'way':
            way_id = element.get('id')
            nd_refs = [nd.get('ref') for nd in element.findall('nd')]
            ways[way_id] = {'nodes': nd_refs}
            for nd_ref in nd_refs:
                node_to_way[nd_ref] = way_id

        elif element.tag == 'relation':
            relation_id = element.get('id')
            members = []
            for member in element.findall('member'):
                member_type = member.get('type')
                ref = member.get('ref')
                role = member.get('role')
                members.append({'type': member_type, 'ref': ref, 'role': role})
                if member_type == 'way':
                    way_to_relation[ref] = relation_id
            relations[relation_id] = {'members': members}

    return nodes, ways, relations, node_to_way, way_to_relation

def find_closest_node(fcd_point, lanelet_nodes, tolerance=0.0001):
    closest_id = None
    min_distance = float('inf')

    for node_id, node in lanelet_nodes.items():
        distance = ((fcd_point['lat'] - node['lat'])**2 + (fcd_point['lon'] - node['lon'])**2)**0.5
        if distance < min_distance and distance <= tolerance:
            min_distance = distance
            closest_id = node_id

    return closest_id

def find_associated_way_and_lanelet(node_id, node_to_way, way_to_relation):
    way_id = node_to_way.get(node_id)
    lanelet_id = way_to_relation.get(way_id)
    return way_id, lanelet_id

# Parse the Lanelet2 data
nodes, ways, relations, node_to_way, way_to_relation = parse_lanelet2_xml('output-file1.osm')

# Load the original FCD XML file
fcd_tree = ET.parse('fcd-output.xml')
fcd_root = fcd_tree.getroot()

# Attributes to remove from each vehicle
attributes_to_remove = ['angle', 'pos','slope', 'acceleration']

# Process each vehicle in each timestep
for timestep in fcd_root.findall('timestep'):
    for vehicle in timestep.findall('vehicle'):
        # Remove unnecessary attributes
        for attr in attributes_to_remove:
            if attr in vehicle.attrib:
                del vehicle.attrib[attr]

        # Process the location data
        fcd_point = {
            'lat': float(vehicle.get('y')),  # Assuming 'y' is latitude
            'lon': float(vehicle.get('x'))   # Assuming 'x' is longitude
        }
        
        closest_node_id = find_closest_node(fcd_point, nodes)
        if closest_node_id:
            vehicle.set('node_id', closest_node_id)
            way_id, lanelet_id = find_associated_way_and_lanelet(closest_node_id, node_to_way, way_to_relation)
            vehicle.set('way_id', way_id if way_id else '')
            vehicle.set('lanelet_id', lanelet_id if lanelet_id else '')
        else:
            vehicle.set('node_id', '')
            vehicle.set('way_id', '')
            vehicle.set('lanelet_id', '')

# Save the modified XML to a new file
fcd_tree.write('modified-fcd-output.xml')






