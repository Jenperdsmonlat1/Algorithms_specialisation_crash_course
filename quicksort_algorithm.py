import random


array = open("array.txt", "r").read().split()
print(array)

int_array = [int(x) for x in array]


def partition(array, left, right):
    
    p = array[left]
    i = left + 1

    for j in range(left + 1, right + 1):

        if array[j] < p:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    temps = array[i - 1]
    array[i - 1] = array[left]
    array[left] = temps
    return i - 1
    

def quicksort(array, left, right):
    
    if left < right:

        pivot = partition(array=array, left=left, right=right)
        quicksort(array=array, left=left, right=pivot-1)
        quicksort(array=array, left=pivot+1, right=right)


if __name__ == "__main__":
    
    quicksort(int_array, 0, len(int_array) - 1)
    print(int_array)
