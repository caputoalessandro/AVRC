import networkx as nx
from resources.resources_path import RESOURCES_PATH


def read_edges(file_name) -> nx.Graph:
    file_path = RESOURCES_PATH / file_name
    fh = open(file_path, "rb")
    G = nx.read_edgelist(fh, nodetype=int)
    fh.close()
    return G


def get_one_node_for_degree_from_list(G : nx.Graph):
    res = {}
    added_degree = []
    for node, d in G.degree():
        if d not in added_degree:
            res.setdefault(node)
            res[node] = d
            added_degree.append(d)
    return res


def get_node_list_from_dict(D : dict, node_list : dict):
    return {
        v : D[k] for k,v in node_list.items()
    }


