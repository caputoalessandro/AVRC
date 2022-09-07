import networkx as nx


def take_measuraments(G):
    APL = nx.average_shortest_path_length(G)


# def get_neighbors_by_degree(G : nx.Graph, node):
#     neighbors = nx.neighbors(G, node)
#
#     neighbors_by_degree = {
#         nx.degree(G, n) : n for n in neighbors
#         }
#
#     return neighbors_by_degree


def distance_k_distribution(G : nx.Graph, k):
    return sum(sum(nx.single_source_shortest_path_length(G, node, k) for node in G.nodes)) / len(G.nodes)
