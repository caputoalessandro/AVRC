import networkx as nx
from resources.resources_path import RESOURCES_PATH
import matplotlib.pyplot as plt
from measures import take_measuraments

edges_file_path = RESOURCES_PATH / "bio_small.edges"


def main():
    # G = nx.read_edgelist(edges_file_path)
    G = nx.fast_gnp_random_graph(20, 0.2, seed=12)
    print_graph(G)
    take_measuraments(G)


def print_graph(G):
    pos = nx.spring_layout(G, seed=47)  # Seed layout for reproducibility
    nx.draw(G, pos=pos)
    plt.show()


if __name__ == "__main__":
    main()