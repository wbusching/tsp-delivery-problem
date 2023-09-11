import networkx as nx

# This function takes as input a graph g and a list of vertices of the cycle.
# (Each vertex given by its index starting from 0.)
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# For example, a valid input would be a graph on 3 vertices and cycle = [2, 0, 1].
#
# The function should return the weight of the cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# If you want to get the weight of the edge between vertices u and v, you can take g[u][v]['weight']


def cycle_weight(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes() # assert statement throws an exception if untrue ("sanity check")
    # Write your code here.
    cycle_weight = 0

    for i in range(len(cycle)): # for each node in the cycle
        v1 = cycle[i] # get the value of this node
        try: 
            v2 = cycle[i+1] # get the value of the next node
        except: 
            v2 = cycle[0] # if this node is the last in the cycle, the next node is the first one

        edge_weight = g[v1][v2]["weight"] # obtain weight of the edge connecting v1 and v2
        cycle_weight += edge_weight # add this edge weight to total cycle weight

    return cycle_weight
    
if __name__ == "__main__":
    # Here is a test case:
    # Create an empty graph. 
    g = nx.Graph()
    # Now we will add 6 edges between 4 vertices
    g.add_edge(0, 1, weight = 2)
    # We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
    g.add_edge(1, 2, weight = 2)
    g.add_edge(2, 3, weight = 2)
    g.add_edge(3, 0, weight = 2)
    g.add_edge(0, 2, weight = 1)
    g.add_edge(1, 3, weight = 1)

    # We now want to compute the lengths of two cycles:
    cycle1 = [0, 1, 2, 3]
    cycle2 = [0, 2, 1, 3]

    assert(cycle_weight(g, cycle1) == 8)
    assert(cycle_weight(g, cycle2) == 6)
    print("success!")