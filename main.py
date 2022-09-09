import networkx as nx
from resources.resources_path import RESOURCES_PATH
from measures import take_measuraments
from plotting import print_graph

edges_file_path = RESOURCES_PATH / "bio_small.edges"


def main():
    G = nx.fast_gnp_random_graph(30, 0.5)
    take_measuraments(G)
    print_graph(G, "Full graph")


if __name__ == "__main__":
    main()