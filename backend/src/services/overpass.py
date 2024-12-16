import requests
import networkx as nx

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_osm_data(min_lat, min_lon, max_lat, max_lon):
    params = {
        'data': f"""
        [out:json];
        (
        way["highway"~"^(motorway|trunk|primary|secondary|tertiary|residential|unclassified|service)$"]({min_lat},{min_lon},{max_lat},{max_lon});
        );
        (._;>;);
        out geom;
        """
    }

    response = requests.post("https://overpass-api.de/api/interpreter", data=params)
    data = response.json()

    gr = nx.Graph()

    nodes = {}
    
    for element in data['elements']:
        if element['type'] == 'node':
            id = element['id']
            lat = element['lat']
            lon = element['lon']
            nodes[id] = (lat, lon)
            gr.add_node(id, pos=(lat, lon))

    for element in data['elements']:
        if element['type'] == 'way':
            nodes_in_way = element['nodes']
            for i in range(len(nodes_in_way)):
                node1 = nodes_in_way[i]
                lat1, lon1 = nodes[node1]
                for j in range(i + 1, len(nodes_in_way)):
                    node2 = nodes_in_way[j]
                    lat2, lon2 = nodes[node2]
                    
                    distance = (lat1 - lat2) ** 2 + (lon1 - lon2) ** 2
                    gr.add_edge(node1, node2, weight=distance)

    return gr
