import heapq


file = open("median.txt", "r").read().split()
int_file = [int(x) for x in file]


def add_numbers(x, low, high):

    if not low or x <= -low[0]:
        heapq.heappush(low, -x)
    else:
        heapq.heappush(high, x)

    if len(low) > len(high) + 1:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) > len(low):
        heapq.heappush(low, -heapq.heappop(high))


def median_maintenance(stream):

    low = []
    high = []
    total = 0

    for x in stream:
        add_numbers(x, low, high)
        
        median = -low[0]
        total += median
    
    return total % 10000


print(median_maintenance(int_file))