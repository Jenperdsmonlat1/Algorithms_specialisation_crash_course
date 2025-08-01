import random

array = open("array.txt", "r").read().split()
int_array = [int(x) for x in array]


def rselect(array, k):

    if len(array) == 1:
        return array[0]
    
    p = random.choice(array)
    left = [x for x in array if x < p]
    right = [x for x in array if x >= p]

    if k <= len(array):
        return rselect(left)