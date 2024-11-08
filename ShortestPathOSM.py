from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
from bridges.color import Color
import os
from minheap import MinHeap
from dotenv import load_dotenv

load_dotenv()
    
#return the vertex the closest to some lat/lon coordinate
def getClosest(gr, lat, lon):
    closest = -1
    min_distance = float('inf')
    
    for vertex in gr.vertices:
        v_lat = gr.get_vertex_data(vertex).latitude
        v_lon = gr.get_vertex_data(vertex).longitude
        distance = (v_lat - lat)**2 + (v_lon - lon)**2
        
        if distance < min_distance:
            min_distance = distance
            closest = vertex

    return closest

#styling the source vertex
def style_root(gr, root):
    gr.get_visualizer(root).color = "red"
    
#shortest path function
def shortestPath(gr, root):
    distance = {vertex: float('inf') for vertex in gr.vertices}
    parent = {vertex: None for vertex in gr.vertices}
    distance[root] = 0

    minheap = MinHeap()
    minheap.insert((0, root))
    while not minheap.is_empty():
        current_distance, current_node = minheap.extractMin()

        if current_distance > distance[current_node]:
            continue

        for neighbor in gr.get_adjacency_list():
            edge = gr.get_edge_data(current_node, neighbor)
            if edge is not None:
                total = current_distance + edge

                if total < distance[neighbor]:
                    distance[neighbor] = total
                    parent[neighbor] = current_node
                    minheap.insert((total, neighbor))

    return (distance, parent)
    
#style the graph based on distance
def style_distance(gr, distance):
    #find the maximum distance which is not infinity
    max_distance = max(d for d in distance.values() if d < float('inf'))

    #style the color of vertices with a linear scale
    for vertex, dist in distance.items():
        if dist < float('inf'):
            intensity = int((1 - dist / max_distance) * 255)
            gr.get_visualizer(vertex).color = Color(255 - intensity, 0, intensity)
        else:
            gr.get_visualizer(vertex).color = "red"
    
#style the path between the root and the destination (root is not given because all parent path goes to root)
def style_parent(gr, parent, dest):  
    # style all vertices to almost invisible
    for vertex in gr.vertices:
        gr.get_visualizer(vertex).color = "lightgray"

    # style all edges to almost invisible
    for vertex in gr.vertices:
        for neighbor in gr.get_adjacency_list():
            if gr.get_edge_data(vertex, neighbor) is not None:
                gr.get_link_visualizer(vertex, neighbor).color = "lightgray"

    # Style the path between parent and dest in black
    ##style node
    current = dest
    while current is not None:
        gr.get_visualizer(current).color = "black"

        ##style edge along the path
        if parent[current] is not None:
            edge = gr.get_edge(parent[current], current)
            if edge is not None:
                edge.color = "black"

        current = parent[current]



def main():
    #get data
    bridges = Bridges(209, "byang564", os.getenv('API_KEY'))

    bridges.set_title("Graph : OpenStreet Map Example")
    bridges.set_description("OpenStreet Map data of Charlotte downtown area, with colors based on distance from the center of downtown")

    #osm_data = data_source.get_osm_data("Charlotte, North Carolina", "primary")
    #osm_data = data_source.get_osm_data("Charlotte, North Carolina", "secondary")
    osm_data = data_source.get_osm_data(35.28, -80.8, 35.34, -80.7, "tertiary"); #UNCC Campus
    
    
    gr = osm_data.get_graph()
    gr.force_large_visualization(True)
    

    #find and style the root of the Shortest Path
    root = getClosest(gr,
                         (osm_data.latitude_range[0]+osm_data.latitude_range[1])/2,
                         (osm_data.longitude_range[0]+osm_data.longitude_range[1])/2)
    style_root(gr, root)
    bridges.set_data_structure(gr)
    bridges.visualize()

    #run Shortest Path
    (distance,parent) = shortestPath(gr,root)

    #style vertices based on distances
    style_distance(gr, distance)
    bridges.set_data_structure(gr)
    bridges.visualize()

    #find a destination
    dest = getClosest(gr,
                      (osm_data.latitude_range[0]+(osm_data.latitude_range[1]-osm_data.latitude_range[0]) / 4),
                      (osm_data.longitude_range[0]+(osm_data.longitude_range[1]-osm_data.longitude_range[0]) / 4))

    #style the path from root to destination
    style_parent(gr,parent, dest)

    bridges.set_data_structure(gr)
    bridges.visualize()


if __name__ == '__main__':
    main()
