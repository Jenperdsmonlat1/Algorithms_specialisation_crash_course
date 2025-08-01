with open("k_clustering_file.txt", "r") as file:
    lines = file.readlines()

node_number = int(lines[0])
graph = []
parents = {i: i for i in range(1, node_number+1)}

for line in lines[1:]:
    contenu = line.split()
    graph.append(((int(contenu[0]), int(contenu[1])), int(contenu[2])))

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


def clustering(graph, clusters):

    graph.sort(key=lambda edge: edge[1])
    spacing = 0
    num_clusters = node_number

    for (u, v), cost in graph:
        if find(u) != find(v):
            if num_clusters > clusters:
                union(u, v)
                num_clusters -= 1
            else:
                spacing = cost
                break

    return spacing

print(clustering(graph=graph, clusters=4))