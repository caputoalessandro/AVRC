from measures import take_measuraments
from plotting import print_graph
from utils import read_edges


def main():
    G = read_edges("bio-yeast-protein-inter.edges")
    # G = G.subgraph(range(100))
    print_graph(G, title="Full_graph")
    take_measuraments(G)
    #
    # nx.drawing.nx_pydot.write_dot(G, RESOURCES_PATH / "test.dot")

    # WRITE FOR GEPHI
    # nx.write_gexf(G, "output/test.gexf")

    #GRAPHVIZ
    # s = Source.from_file(RESOURCES_PATH / "test.dot")
    # s.view()
    return


if __name__ == "__main__":
    main()