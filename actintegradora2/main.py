# Integrative Activity 2
# Marco Torres
# Uriel Aguilar
# Fer Valdeòn
# Diego Araque
# November 24, 2022


def read_graph():
    '''Function that reads a graph in the adyacent matrix form.'''
    with open("./graph.txt") as f:
        n_vertices = int(f.readline())
        graph = [[int(x) for x in line.split(" ") if not x == ''] for line in f.readlines()]
        return n_vertices, graph


def mst(n_vertices, graph):
    '''Function that returns the minimum spanning tree of a graph using Prim's algorithm.'''

    visited_nodes = [0] * n_vertices # Array that checks if the node is visited
    visited_nodes[0] = 1 # Init first node as visited

    results = [] # Matrix to store the results [start node, end node, weight]
    available_edges = {} # Available edges of the visited nodes

    i = 0 # Start with the first node of the matrix

    # While there are unvisited nodes
    while sum(visited_nodes) < n_vertices:

        # Iterate this nodes edges to store them in available edges
        for j in range(len(graph[i])):
            # Ignore if there is an edge to the same node
            if i == j:
                continue
            # Ignore if there is no edge
            if graph[i][j] == 0:
                continue
            # Add node edge in form => weight: [start node, end node]
            available_edges[graph[i][j]] = [i, j]

        # Get min edge from all the available edges
        minimum = 100000000000
        for key in available_edges:
            # Check if the node of the edge is already visited, if so ignore it
            node_index = available_edges[key][1]
            if visited_nodes[node_index]:
                continue
            # Check if is new min
            if key < minimum:
                minimum = key
        
        # If minimum is diferent from infinity
        if minimum != 100000000000:
            # Store new minimum edge
            min_edge = available_edges[minimum]
            results.append([min_edge[0], min_edge[1], minimum])
            i = min_edge[1] # Process the node of the new edge
            
        # Set cur node as visited
        visited_nodes[i] = 1

    return results


def print_res(results):
    '''Function that prints the given results.'''
    for res in results:
        print(f"From town {res[0]} to town {res[1]}: Distance {res[2]} km")

    
if __name__ == "__main__":
    n_vertices, graph = read_graph()
    result = mst(n_vertices, graph)
    print_res(result)