"""
We implement the brute force algorithm for the TSP, checking all
permutations of vertices and returning the minimum weight of a cycle
that visits each vertex exactly once.
"""


import networkx as nx
from itertools import permutations
from cycle-weight import cycle_length

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Iterate through all permutations of n vertices
    #for p in permutations(range(n)):
        # Write your code here.

    return ???
