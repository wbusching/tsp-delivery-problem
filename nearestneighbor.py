"""
This function implements the nearest neighbor algorithm, 
a greedy algorithm for finding the solution to the TSP.
Note that this algorithm is efficient, executing in 
polynomial time.

This function takes as input a graph g.
The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
and has no self-loops (i.e., there are no edges from i to i).

The function should return the weight of the nearest neighbor heuristic, which starts at the vertex number 0,
and then each time selects a closest vertex.

"""

import networkx as nx

def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times, once for each remaining vertex to hit
    for i in range(n - 1):
        next_node = None # the nearest neighbor
        min_edge = float("inf") # The distance to the nearest neighbor. Initialized with infinity.

        for v in g.nodes():
            # Write your code here: decide if v is a better candidate than next_node.
            # If it is, then update the values of next_node and min_edge
            if v in path:
                continue
            else:
                new_edge_weight = g[current_node][v]["weight"] # obtain weight of the edge connecting current node to v

                if new_edge_weight < min_edge:
                    next_node = v
                    min_edge = new_edge_weight
            
        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight
