import networkx as nx
import time
from src.services.minheap import MinHeap
from src.services.fibheap import FibonacciHeap
from src.services.overpass import get_osm_data

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
    
#return the vertex the closest to some lat/lon coordinate
def getClosest(gr, lat, lon):
    closest = None
    min_distance = float('inf')
    
    for node, (node_lat, node_lon) in nx.get_node_attributes(gr, 'pos').items():
        distance = ((node_lat - lat) ** 2 + (node_lon - lon) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest = node
    
    return closest
    
#shortest path function
def shortestPathMin(gr, root):
    distance = {node: float('inf') for node in gr.nodes}
    parent = {node: None for node in gr.nodes}
    distance[root] = 0

    minheap = MinHeap()
    minheap.insert((0, root))
    while not minheap.is_empty():
        current_distance, current_node = minheap.extract_min()

        if current_distance > distance[current_node]:
            continue

        for neighbor in gr.neighbors(current_node):
            edge = gr[current_node][neighbor]['weight']
            total = current_distance + edge

            if total < distance[neighbor]:
                distance[neighbor] = total
                parent[neighbor] = current_node
                minheap.insert((total, neighbor))

    return parent

#shortest path function with fib heap
def shortestPathFib(gr, root):
    distance = {node: float('inf') for node in gr.nodes}
    parent = {node: None for node in gr.nodes}
    distance[root] = 0

    fibheap = FibonacciHeap()
    fibheap.insert((0, root))
    while not fibheap.is_empty():
        current_distance, current_node = fibheap.extract_min()

        if current_distance > distance[current_node]:
            continue

        for neighbor in gr.neighbors(current_node):
            edge = gr[current_node][neighbor]['weight']
            total = current_distance + edge
            if total < distance[neighbor]:
                distance[neighbor] = total
                parent[neighbor] = current_node
                fibheap.insert((total, neighbor))


    return parent

def ShortestPath(start, end, data_structure):
    #get data
    min_lat = min(start['lat'], end['lat'])
    min_lon = min(start['lon'], end['lon'])
    max_lat = max(start['lat'], end['lat'])
    max_lon = max(start['lon'], end['lon'])

    gr = get_osm_data(min_lat - 0.1, min_lon - 0.1, max_lat + 0.1, max_lon + 0.1)

    #find the root of the Shortest Path
    root = getClosest(gr, start['lat'], start['lon'])
    
    #find a destination
    dest = getClosest(gr, end['lat'], end['lon'])

    #uses dijkstras while logging time
    start = time.time()

    if data_structure == 'fibheap':
        parent = shortestPathFib(gr,root)
    else:
        parent = shortestPathMin(gr,root)

    logger.debug(time.time() - start)

    #find path from root to dest
    path = []
    current = dest
    while current is not None:
        path.append(gr.nodes[current]['pos'])
        current = parent[current]
    path.reverse()

    return path