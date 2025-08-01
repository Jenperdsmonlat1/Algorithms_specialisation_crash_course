from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)



"""
function knapsack(values, weights, W):
    n = length(values)
    dp = array of size (n+1) × (W+1) initialized to zero

    for i from 1 to n:
        for w from 0 to W:
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]  # objet trop lourd → on l'ignore
            else:
                dp[i][w] = max(
                    dp[i-1][w],                      # on ignore l'objet i
                    dp[i-1][w - weights[i-1]] + values[i-1]  # on inclut l'objet i
                )

    return dp[n][W]  # valeur optimale
"""


with open("knapsack_big.txt", "r") as file:
    lines = file.readlines()


bag_size, article_number = lines[0].split()
articles = defaultdict(list)
cache = {}

for line in lines[1:]:
    articles["value"].append(int(line.split()[0]))
    articles["weight"].append(int(line.split()[1]))


def knapsack(values, weights, W):

    n = len(values)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(0, W + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
    
    return dp[n][w]

def knapsack_recursive(i, W):

    if i == 0:
        return 0
    if (i, W) in cache:
        return cache[(i, W)]
    
    if articles["weight"][i - 1] > W:
        result = knapsack_recursive(i - 1, W)
    else:
        result = max(
            knapsack_recursive(i - 1, W),
            knapsack_recursive(i - 1, W - articles["weight"][i - 1]) + articles["value"][i - 1]
        )

    cache[(i, W)] = result
    return result

print(knapsack_recursive(int(article_number), int(bag_size)))
