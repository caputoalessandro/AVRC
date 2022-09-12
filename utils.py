import networkx as nx
from resources.resources_path import RESOURCES_PATH
import graphviz


def read_edges(file_name) -> nx.Graph:
    file_path = RESOURCES_PATH / file_name
    fh = open(file_path, "rb")
    G = nx.read_edgelist(fh, nodetype=int)
    fh.close()
    return G

