import networkx as nx
from collections import defaultdict
import sys


sys.setrecursionlimit(10**6)


graph = defaultdict(list)
graph_reverse = defaultdict(list)

with open("file_graph.txt", "r") as file:
    for line in file:
        tail, head = map(int, line.split())
        graph[tail].append(head)
        graph_reverse[head].append(tail)


def DFS_first_pass(graph_rev, v, finish_order, explored):
    explored[v] = True

    for u in graph_rev[v]:
        if explored[u] == False:
            DFS_first_pass(graph_rev, u, finish_order, explored)
    
    finish_order.append(v)


def DFS_second_pass(graph, u, component, explored):
    explored[u] = True
    component.append(u)
    for v in graph[u]:
        if explored[v] == False:
            DFS_second_pass(graph, v, component, explored)


def kasaraju(graph, graph_reverse):

    nodes = set(graph) | set(graph_reverse)
    explored = {v: False for v in nodes}
    finish_order = []

    for v in sorted(nodes, reverse=True):
        if explored[v] == False:
            DFS_first_pass(graph_reverse, v, finish_order, explored)

    for v in graph:
        explored[v] = False
    
    explored = {v: False for v in nodes}
    scc_list = []
    for v in reversed(finish_order):
        if explored[v] == False:
            component = []
            DFS_second_pass(graph, v, component, explored)
            scc_list.append(component)

    return scc_list

scc = kasaraju(graph, graph_reverse)
sizes = sorted([len(c) for c in scc], reverse=True)
while len(sizes) < 5:
    sizes.append(0)

print(",".join(map(str, sizes)))