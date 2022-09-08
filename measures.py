import networkx as nx
from collections import Counter
from statistics import pvariance, pstdev


def take_measuraments(G):
    N = len(G.nodes)

    # distance
    # APL = nx.average_shortest_path_length(G)
    # distance_distributon = distance_distributions(G,N)

    # degree
    degree_distribution = [i for _, i in G.degree]
    average_degree = get_average_degree(N, degree_distribution)
    degree_variance = pvariance(degree_distribution)
    degree_standard_deviation = pstdev(degree_variance)
    return


def get_max_degree(G:nx.Graph):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    return max(degree_sequence)


def get_distance_distributions(G : nx.Graph, N):
    paths_dict = dict(nx.all_pairs_shortest_path_length(G))
    lenghts = [value for k in paths_dict.values() for value in k.values()]
    k_distances = Counter(lenghts)
    return {int(k): val/N for k, val in k_distances.items()}


def get_average_degree(N, degree_distribution):
    degree_sum = sum(degree_distribution)
    return degree_sum/N


