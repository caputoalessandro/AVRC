import networkx as nx
from resources.resources_path import RESOURCES_PATH
import matplotlib.pyplot as plt

edges_file_path = RESOURCES_PATH / "bio_small.edges"


def main():
    # G = nx.read_edgelist(edges_file_path)
    G = nx.complete_graph(5)

    # G = nx.path_graph(8)
    pos = nx.spring_layout(G, seed=47)  # Seed layout for reproducibility
    nx.draw(G, pos=pos)
    plt.show()


# def print_graph():
#     G = nx.petersen_graph()
#     pos = nx.spring_layout(G)
#     subax1 = plt.subplot(121)
#     nx.draw(G, with_labels=True, font_weight='bold')
#     subax2 = plt.subplot(122)
#     nx.draw_shell(G, pos=nx.spring_layout(G), with_labels=True, font_weight='bold')


if __name__ == "__main__":
    main()