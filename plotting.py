import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import random


def plot_distribution(distribution: dict, title, xlabel,ylabel):
    plt.figure()
    sns.set_theme()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(distribution.keys(), distribution.values())
    # plt.show()
    plt.savefig('output/'+str(title))
    # print(str(title)+" plot saved in 'output")
    return


def print_graph(G, title):
    plt.figure()
    pos = nx.spring_layout(G, seed=47)  # Seed layout for reproducibility
    plt.title(title)
    nx.draw(G, pos=pos)
    # plt.show()
    plt.savefig('output/' + str(title))
    return


def print_subgraphs(G, subG, title):
    plt.figure()
    plt.title(title)
    pos = nx.spring_layout(G, seed=47)
    nx.draw(G, pos=pos, node_color='#6495ED')
    nx.draw(subG, pos=pos, node_color="#DC143C")
    plt.savefig('output/'+str(title))
    # print("largest conneted component plot saved in 'output'")
    return


def print_communities(G, communities, k):
    plt.figure()
    step = 1
    for community in communities:
        plt.title("Communities: step " + str(step))
        pos = nx.spring_layout(G, seed=47)
        nx.draw(G, pos=pos, node_color='#6495ED')
        for e in community:
            pos = nx.spring_layout(G, seed=47)
            subG = G.subgraph(e)
            nx.draw(subG, pos=pos, node_color=get_random_color())
        # plt.show(block=False)
        plt.savefig('output/communities/step_' + str(step))
        step = step + 1

        if len(community) > k:
            # print("Comunnities plots saved in output/communities")
            return

    # print("\nCommunities plots saved in 'output/communities'")
    return


def get_random_color():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


