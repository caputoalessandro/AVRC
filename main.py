import networkx as nx
from resources.resources_path import RESOURCES_PATH
from measures import take_measuraments
from plotting import print_graph

edges_file_path = RESOURCES_PATH / "bio_small.edges"


def main():
    G = nx.karate_club_graph()
    take_measuraments(G)
    print_graph(G, "Full graph")


if __name__ == "__main__":
    main()