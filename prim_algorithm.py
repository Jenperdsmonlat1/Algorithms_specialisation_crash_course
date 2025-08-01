import heapq
from collections import defaultdict

graph = defaultdict(list)

# Lecture du fichier
with open("prim.txt") as f:
    lines = f.readlines()

n_nodes, n_edges = map(int, lines[0].split())

# Construction du graphe
for line in lines[1:]:
    u, v, cost = map(int, line.split())
    graph[u].append((cost, v))
    graph[v].append((cost, u))  # Graphe non orienté

# Initialisation de Prim
visited = set()
min_heap = []
start_node = 1
visited.add(start_node)

for edge in graph[start_node]:
    heapq.heappush(min_heap, edge)

total_cost = 0

while len(visited) < n_nodes:
    cost, node = heapq.heappop(min_heap)
    if node in visited:
        continue
    visited.add(node)
    total_cost += cost

    for edge in graph[node]:
        heapq.heappush(min_heap, edge)

print("Coût total de l’arbre couvrant minimal :", total_cost)
