import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import copy
import random



graph = defaultdict(list)

with open("file.txt", "r") as file:

    for line in file:
        parts = list(map(int, line.strip().split()))
        node = parts[0]
        neighbors = parts[1:]
        graph[node].extend(neighbors)

G = nx.Graph()
for u in graph:
    for v in graph[u]:
        G.add_edge(u, v)


def min_cut(graph):

    node = copy.deepcopy(graph)

    while len(node) > 2:

        u = random.choice(list(node.keys()))
        v = random.choice(node[u])

        node[u].extend(node[v])

        for key in node:
            node[key] = [u if x == v else x for x in node[key]]
    
        node[u] = [x for x in node[u] if x != u]
        del node[v]

    return len(list(node.values())[0])


def repeated_karger(graph, num_trials):
    mincut = float('inf')
    for _ in range(num_trials):
        cut = min_cut(graph)
        mincut = min(mincut, cut)

    return mincut

mincut = repeated_karger(graph=graph, num_trials=1000)
print(mincut)

plt.figure()
nx.draw(G, with_labels=True, node_size=400, node_color='green')
plt.show()