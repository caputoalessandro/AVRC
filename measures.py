import networkx as nx
from collections import Counter


def get_max_degree(G):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    return max(degree_sequence)


def distance_distributions(G : nx.Graph):
    graph_dim = len(G.nodes)
    paths_dict= dict(nx.all_pairs_shortest_path_length(G))
    lenghts = [value for k in paths_dict.values() for value in k.values() ]
    k_distances = Counter(lenghts)
    return {int(k): val/graph_dim for k, val in k_distances.items()}


def take_measuraments(G):
    APL = nx.average_shortest_path_length(G)
    distance_distributon = distance_distributions(G)
    print(APL)
    print(distance_distributon)

