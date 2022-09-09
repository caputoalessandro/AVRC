import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx


def plot_distribution(distribution: dict, title, xlabel,ylabel):
    sns.set_theme()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(distribution.keys(), distribution.values())
    plt.show()


def print_graph(G, title):
    pos = nx.spring_layout(G, seed=47)  # Seed layout for reproducibility
    plt.title(title)
    nx.draw(G, pos=pos)
    plt.show()


def print_subgraphs(G, subG, title):
    plt.title(title)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, node_color='#6495ED')
    nx.draw(subG, pos=pos, node_color="#DC143C")
    plt.show()


