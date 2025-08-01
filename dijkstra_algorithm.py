from collections import defaultdict


graph = defaultdict(list)

with open("graph_dijkstra.txt", "r") as file:
    for line in file:
        tokens = line.strip().split()
        index = int(tokens[0])
        aretes = list(map(lambda x: (int(x.split(',')[0]), int(x.split(',')[1])), tokens[1:]))

        if index not in graph:
            graph[index] = []
        
        for neighbors, weight in aretes:
            graph[index].append((neighbors, weight))

            if neighbors not in graph:
                graph[neighbors] = []
            graph[neighbors].append((index, weight))

def dijkstra(graph, s):

    distance = {}
    precedent = {}
    Q = set(graph.keys())

    for v in graph:
        distance[v] = float('inf')
        precedent[v] = None
    
    distance[s] = 0

    while Q:
        u = min(Q, key=lambda v: distance[v])
        Q.remove(u)


        for neighbors, weights in graph.get(u, []):
            if neighbors in Q:
                alt = distance[u] + weights
                if alt < distance[neighbors]:
                    distance[neighbors] = alt
                    precedent[neighbors] = u
    
    return distance


distances = dijkstra(graph, 1)
targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
result = [distances.get(v, 1000000) for v in targets]
print(','.join(str(d) for d in result))

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for u in graph:
    for v, w in graph[u]:
        G.add_edge(u, v, weight=w)

nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()