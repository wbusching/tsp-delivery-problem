"""
This function computes the average weight of a graph's Hamiltonian cycle,
using the formula from lemma given.

We assume the graph is complete, undirected, and has no self-loops.
"""


def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    # Write your code here.
    return 2 * sum_of_weights / (n-1)