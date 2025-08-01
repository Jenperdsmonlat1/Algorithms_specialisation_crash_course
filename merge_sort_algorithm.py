

fichier = open("file.txt", "r")
contenu = fichier.read().split()
int_numbers = [int(x) for x in contenu]



def merge(array, left, mid, right):

    n1 = mid - left + 1
    n2 = right - mid

    Left = array[left : mid + 1]
    Right = array[mid + 1 : right + 1]

    i = 0
    j = 0
    k = left
    inversion = 0

    while i < n1 and j < n2:

        if Left[i] <= Right[j]:
            array[k] = Left[i]
            i += 1
        else:
            array[k] = Right[j]
            j += 1
            inversion += n1 - i
        k += 1
    
    while i < n1:
        array[k] = Left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = Right[j]
        j += 1
        k += 1
    
    return inversion


def merge_sort(array, left, right):

    if left < right:

        mid = (left + right) // 2
        left_count = merge_sort(array, left, mid)
        right_count = merge_sort(array, mid + 1, right)
        merge_count = merge(array, left, mid, right)
        return left_count + right_count + merge_count
    else:
        return 0

value = merge_sort(int_numbers, 0, len(int_numbers) - 1)
print(value)