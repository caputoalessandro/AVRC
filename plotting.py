import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import random
from itertools import islice
import os

DIR = "output/communities/"


def plot_distribution(distribution: dict, title, xlabel, ylabel, x_size=6.4, y_size=4.8):
    os.makedirs(os.path.dirname(DIR), exist_ok=True)
    plt.figure(figsize=(x_size, y_size), dpi=500)
    sns.set_theme()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.bar(distribution.keys(), distribution.values())
    plt.savefig('output/'+str(title) + ".pdf")
    return


def draw_graph(G, subG=None, title="", node_s=1, w=0.1):
    plt.figure(figsize=(20, 14))
    plt.axis('off')
    plt.title(title)
    pos = nx.spring_layout(G, seed=47)
    nx.draw(G, pos=pos, node_color='#6495ED', node_size=node_s, width=w)
    if subG:
        nx.draw(subG, pos=pos, node_color="#DC143C", node_size=node_s, width=w)
    return


def print_graph(G, subG=None, title="", node_s=1, w=0.1):
    os.makedirs(os.path.dirname(DIR), exist_ok=True)
    draw_graph(G, subG, title, node_s, w)
    plt.savefig('output/ ' + str(title) + ".pdf", dpi=1000)
    return


def print_communities(G, c_generator, k):
    os.makedirs(os.path.dirname(DIR), exist_ok=True)
    step = 1
    pos = nx.spring_layout(G, seed=47)
    for communities in islice(c_generator, k):
        draw_graph(G, None, title="Communities: step " + str(step))
        for c in communities:
            subG = G.subgraph(c)
            nx.draw(subG, pos, node_color=get_random_color(), node_size=1, width=0.1)
        plt.savefig('output/communities/step_' + str(step) + ".pdf", dpi=1000)
        step = step + 1
    return


# def print_communities(G, communities, k):
#     plt.figure(figsize=(20, 14))
#     plt.axis('off')
#     pos = nx.spring_layout(G, seed=47)
#     step = 1
#
#     for community in islice(communities, k):
#         plt.title("Communities: step " + str(step))
#         nx.draw(G, pos=pos, node_color='#6495ED', node_size=100, width=1)
#         for e in community:
#             subG = G.subgraph(e)
#             nx.draw(subG, pos=pos, node_color=get_random_color(), node_size=100, width=1)
#
#         plt.savefig('output/communities/step_' + str(step),dpi=1000)
#         step = step + 1
#
#         if len(community) > k:
#             return
#     return


def get_random_color():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


