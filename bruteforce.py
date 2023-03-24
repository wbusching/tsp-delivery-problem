"""
We implement the brute force algorithm for the TSP, checking all
permutations of vertices and returning the minimum weight of a cycle
that visits each vertex exactly once.
"""


import networkx as nx
from itertools import permutations
from random import choice

# import our pre-built function to compute cycle weight!
from cycleweight import cycle_weight 

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def brute_force_tsp(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # use the weight of a random permutation as the initial min_weight
    # recall, this is very unlikely to be near-optimal
    perms = permutations(range(n))               # `permutations` returns a container of all permutations, expressed as tuples
    min_weight = cycle_weight(g, choice(list(perms)))  # compute cycle weight for a random permutation

    for p in perms:     
        p_weight = cycle_weight(g, p)    # compute the weight of the cycle represented by this permutation

        if (p_weight < min_weight):      # check if this weight is smaller than the running min weight
            min_weight = p_weight        # update running min weight if so

    return min_weight



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

    # Now we want to compute the lengths of two cycles:
    cycle1 = [0, 1, 2, 3]
    cycle2 = [0, 2, 1, 3]

    assert(cycle_weight(g, cycle1) == 8)
    assert(cycle_weight(g, cycle2) == 6)
    

    print(brute_force_tsp(g))