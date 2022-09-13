import networkx as nx
from collections import Counter
from plotting import plot_distribution, print_communities, print_graph
from statistics import pvariance
from math import sqrt
from utils import get_one_node_for_degree_from_list, get_node_list_from_dict


def take_measuraments(G : nx.Graph):
    N = len(G.nodes)

    # print("Degree measuraments")
    # degree_measurements(G, N)

    # print("Clustering measuraments")
    # # clustering coefficent
    # clustering_coefficent = nx.average_clustering(G)
    # print("Clustering coefficent: ", "%.3f" % clustering_coefficent)
    # # plot_distribution(clustering_coefficent, "Clustering coefficent", "Vertex", "Coefficent",100,10)

    # print("Largest connected component measurament")
    # # largest connected component
    # largest_cc = max(nx.connected_components(G), key=len)
    # largest_cc_sub = G.subgraph(largest_cc)
    # print_graph(G, largest_cc_sub, title="Largest_connected_component")

    # # print("Distances measuraments")
    # # distance_measurements(G, N, largest_cc_sub)
    #
    # print("Degree correlation measurament")
    # # degree correlation
    # r = nx.degree_pearson_correlation_coefficient(G)
    # print("Degree correlation: ", "%.2f" % r)

    # print("communities calculation")
    # # communnities
    # # subgraph = G.edge_subgraph(largest_cc_sub.edges(range(0, 10)))
    # subgraph = largest_cc_sub
    # communities_generator = nx.community.girvan_newman(subgraph)
    # print_communities(subgraph, communities_generator, 3)

    # print("centralities measuraments")
    centralities(G)

    # print("\nPlots saved in output folder")

    return


def distance_distributions(G : nx.Graph, N):
    paths_dict = dict(nx.all_pairs_shortest_path_length(G))
    lenghts = [value for k in paths_dict.values() for value in k.values()]
    counts = Counter(lenghts)
    return {str(k): val / N for k, val in counts.items()}


def average_degree(G,N):
    degree_sum = sum(i for _, i in G.degree)
    return degree_sum/N


def distance_measurements(G, N, LCC):
    AD = nx.average_shortest_path_length(LCC)
    DistanceD = distance_distributions(G, N)
    plot_distribution(DistanceD, "Distance distribution", "Distance", "Frequency")
    print("Average distance: ", "%.2f" % AD)
    return


def degree_measurements(G, N):
    DegreeD = degree_distribution(G, N)
    plot_distribution(DegreeD, "Degree distribution", "Degree", "Frequency")

    AD = average_degree(G,N)
    print("Average degree: ", "%.2f" % AD)

    degree_variance = pvariance(DegreeD.values())
    print("Degree variance: ", "%.4f" % degree_variance)

    degree_standard_deviation = sqrt(degree_variance)
    print("Degree standard deviation: ", "%.4f" % degree_standard_deviation)
    return


def degree_distribution(G, N):
    degrees = [i for _, i in G.degree]
    degree_counts = Counter(degrees)
    ordered_d = sorted(degree_counts.items())
    return {k: val / N for k, val in ordered_d}


def centralities(G : nx.Graph):
    DC = nx.degree_centrality(G)
    CC = nx.closeness_centrality(G)
    BC = nx.betweenness_centrality(G)

    nodes = get_one_node_for_degree_from_list(G)
    DC_to_plot = get_node_list_from_dict(DC, nodes)
    CC_to_plot = get_node_list_from_dict(CC, nodes)
    BC_to_plot = get_node_list_from_dict(BC, nodes)

    plot_distribution(DC_to_plot, "Degree centrality", "Degree", "centrality")
    plot_distribution(CC_to_plot, "Closeness centrality", "Degree", "centrality")
    plot_distribution(BC_to_plot, "Betweeness centrality", "Degree", "centrality")
    return
