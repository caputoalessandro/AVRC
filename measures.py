import networkx as nx
from collections import Counter


def get_max_degree(G):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    return max(degree_sequence)


def distance_distribution(G : nx.Graph):
    graph_dim = len(G.nodes)
    paths_iterator = nx.all_pairs_shortest_path_length(G)
    lenghts = [paths_iterator[i][j] for i in range(graph_dim) for j in range(graph_dim)]
    k_distances = Counter(lenghts)
    return {int(k): val/graph_dim for k, val in k_distances.items()}


def take_measuraments(G):
    APL = nx.average_shortest_path_length(G)
    distance_distributon = distance_distribution(G)
    print(APL)
    print(distance_distributon)

