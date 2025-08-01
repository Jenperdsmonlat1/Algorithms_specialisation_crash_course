import heapq


"""
function HuffmanMaxDepth(weights):
    # Étape 1 : Initialisation de la file de priorité
    create a min_heap
    for each weight in weights:
        insert Node(weight) into min_heap

    # Étape 2 : Construction de l'arbre
    while min_heap.size > 1:
        node1 = min_heap.extract_min()
        node2 = min_heap.extract_min()
        merged = Node(node1.weight + node2.weight)
        merged.left = node1
        merged.right = node2
        min_heap.insert(merged)

    # Étape 3 : Parcours pour trouver la profondeur maximale
    root = min_heap.extract_min()

    return maxDepth(root)

function maxDepth(node, depth=0):
    if node is leaf:
        return depth
    else:
        return max(
            maxDepth(node.left, depth + 1),
            maxDepth(node.right, depth + 1)
        )
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __lt__(self, other):
        return self.value < other.value


with open("huffman.txt", "r") as file:
    lines = file.readlines()

symbol_number = int(lines[0])

weights = [int(x) for x in lines[1:]]


def maxDepth(node, depth=0):

    if node.is_leaf():
        return depth
    else:
        return max(
            maxDepth(node.left, depth + 1),
            maxDepth(node.right, depth + 1))

def minDepth(node, depth=0):

    if node.is_leaf():
        return depth
    else:
        return min(
            minDepth(node.left, depth + 1),
            minDepth(node.right, depth + 1))

def huffman_max_depth(weights):

    min_heap = []
    heapq.heapify(min_heap)

    for weight in weights:
        node = Node(weight)
        heapq.heappush(min_heap, node)
    
    while len(min_heap) > 1:
        node1 = heapq.heappop(min_heap)
        node2 = heapq.heappop(min_heap)
        merged = Node(node1.value + node2.value)
        merged.left = node1
        merged.right = node2
        heapq.heappush(min_heap, merged)

    min_value = heapq.heappop(min_heap)
    return minDepth(min_value)

print(huffman_max_depth(weights=weights))
