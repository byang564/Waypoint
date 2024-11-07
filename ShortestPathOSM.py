from bridges.data_src_dependent import data_source
from bridges.bridges import Bridges
import os
import queue as Q
from dotenv import load_dotenv

load_dotenv()
    
#return the vertex the closest to some lat/lon coordinate
def getClosest(gr, lat, lon):
    # TODO
    closest = -1
    min = float('inf')
    for vertex in gr.get_vertices():
        vertex_lat = vertex.get_lat()
        vertex_lon = vertex.get_lon()
        distance = ((lat - vertex_lat) ** 2 + (lon - vertex_lon) ** 2)
        if distance < min:
            min = distance
            closest = vertex.get_id()

    return closest

#styling the source vertex
def style_root(gr, root) :
    # TODO
    vertex = gr.get_vertex(root)
    vertex.set_color("red")
    
#shortest path function
def shortestPath (gr, root) :
    distance = {}
    parent = {}

    #TODO

    return (distance, parent)
    
#style the graph based on distance
def style_distance(gr, distance):
    #TODO
    #find the maximum distance which is not infinity

    #style the color of vertices with a linear scale
    pass
    
#style the path between the root and the destination (root is not given because all parent path goes to root)
def style_parent(gr, parent, dest):
    #TODO
    
    # style all vertices to almost invisible

    # style all edges to almost invisible

    # Style the path between parent and dest in black
    ##style node

    ##style edge along the path
    pass
    
def main():
    #get data
    bridges = Bridges(209, "byang564", os.getenv('API_KEY'))

    bridges.set_title("Graph : OpenStreet Map Example")
    bridges.set_description("OpenStreet Map data of Charlotte downtown area, with colors based on distance from the center of downtown")

    #TODO: Get Data
    #osm_data = data_source.get_osm_data("Charlotte, North Carolina", "primary")
    #osm_data = data_source.get_osm_data("Charlotte, North Carolina", "secondary")
    osm_data = data_source.get_osm_data(35.28, -80.8, 35.34, -80.7, "tertiary"); #UNCC Campus
    
    
    gr = osm_data.get_graph()
    gr.force_large_visualization(True)
    

    #TODO: Uncomment for part 2
    # #find and style the root of the Shortest Path
    # root = getClosest(gr,
    #                      (osm_data.latitude_range[0]+osm_data.latitude_range[1])/2,
    #                      (osm_data.longitude_range[0]+osm_data.longitude_range[1])/2)
    # style_root(gr, root)
    # bridges.set_data_structure(gr)
    # bridges.visualize()

    #TODO: Uncomment for part 3
    # #run Shortest Path
    #(distance,parent) = shortestPath(gr,root)

    # #style vertices based on distances
    # style_distance(gr, distance)
    # bridges.set_data_structure(gr)
    # bridges.visualize()

    #TODO Uncomment for part 4
    # #find a destination
    # dest = getClosest(gr,
    #                   (osm_data.latitude_range[0]+(osm_data.latitude_range[1]-osm_data.latitude_range[0])/4),
    #                   (osm_data.longitude_range[0]+(osm_data.longitude_range[1]-osm_data.longitude_range[0])/4))

    # #style the path from root to destination
    # style_parent(gr,parent, dest)

    # bridges.set_data_structure(gr)
    # bridges.visualize()


if __name__ == '__main__':
    main()
