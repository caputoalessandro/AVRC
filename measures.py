import networkx as nx
from collections import Counter
from plotting import plot_distribution, print_subgraphs, print_communities
from statistics import pvariance
from math import sqrt


def take_measuraments(G):
    N = len(G.nodes)

    distance_measurements(G, N)

    degree_measurements(G, N)

    # clustering coefficent
    clustering_coefficent = nx.clustering(G)
    plot_distribution(clustering_coefficent, "Clustering coefficent", "Vertex", "Coefficent")

    # largest connected component
    largest_cc = max(nx.connected_components(G), key=len)
    component = G.subgraph(largest_cc)
    print_subgraphs(G, component, "Largest connected  component")

    # degree correlation
    r = nx.degree_pearson_correlation_coefficient(G)
    print("Degree correlation: ", "%.2f" % r)

    # communnities
    communities_generator = nx.community.girvan_newman(G)
    print_communities(G, communities_generator, 10)

    centralities(G)

    print("\nPlots saved in output folder")

    return


def distance_distributions(G : nx.Graph, N):
    paths_dict = dict(nx.all_pairs_shortest_path_length(G))
    lenghts = [value for k in paths_dict.values() for value in k.values()]
    counts = Counter(lenghts)
    return {str(k): val / N for k, val in counts.items()}


def average_degree(N, degree_distribution):
    degree_sum = sum(degree_distribution)
    return degree_sum/N


def distance_measurements(G, N):
    AD = nx.average_shortest_path_length(G)
    DistanceD = distance_distributions(G, N)
    plot_distribution(DistanceD, "Distance distribution", "Distance", "Frequency")
    print("Average distance: ", "%.2f" % AD)
    return

def degree_measurements(G, N):
    DegreeD = degree_distribution(G, N)
    plot_distribution(DegreeD, "Degree distribution", "Degree", "Frequency")

    AD = average_degree(N, DegreeD.values())
    print("Average degree: ", "%.2f" % AD)

    degree_variance = pvariance(DegreeD.values())
    print("Degree variance: ", "%.4f" % degree_variance)

    degree_standard_deviation = sqrt(degree_variance)
    print("Degree standard deviation: ", "%.4f" % degree_standard_deviation)
    return

def degree_distribution(G,N):
    degrees = [i for _, i in G.degree]
    degree_counts = Counter(degrees)
    ordered_d = sorted(degree_counts.items())
    return {k: val / N for k, val in ordered_d}


def centralities(G):
    DC = nx.degree_centrality(G)
    CC = nx.closeness_centrality(G)
    BC = nx.betweenness_centrality(G)
    plot_distribution(DC, "Degree distribution", "Nodes", "centrality")
    plot_distribution(CC, "Closeness centrality", "Nodes", "centrality")
    plot_distribution(BC, "Betweeness centrality", "Edges", "centrality")
    return
