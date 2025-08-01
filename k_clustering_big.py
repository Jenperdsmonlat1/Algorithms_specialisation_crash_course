from itertools import combinations
from collections import defaultdict

nodes = defaultdict(list)

with open("clustering_big.txt", "r") as file:
    n, bits = map(int, file.readline().split())
    for index, line in enumerate(file, 1):
        label = int("".join(line.strip().split()), 2)
        nodes[label].append(index)


parents = {i: i for i in range(1, n+1)}


def hamming_distance(label, bits):

    neighbors = []
    for i in range(bits):
        neighbors.append(label ^ (1 << i))
    
    for i, j in combinations(range(bits), 2):
        neighbors.append(label ^ (1 << i) ^ (1 << j))
    
    return neighbors

def find(i):

    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    
    return i

def union(i, j):

    pi, pj = find(i), find(j)
    if pi != pj:
        parents[pi] = pj
        return True
    
    return False

for label, node_ids in nodes.items():
    for i in range(len(node_ids)):
        for j in range(i + 1, len(node_ids)):
            union(node_ids[i], node_ids[j])
    for node_id in node_ids:
        for neighbor in hamming_distance(label, bits):
            if neighbor in nodes:
                for other_id in nodes[neighbor]:
                    union(node_id, other_id)

final_clusters = set(find(node) for node in parents)
print("Nombre de grappes k avec espacement ≥ 3 :", len(final_clusters))
