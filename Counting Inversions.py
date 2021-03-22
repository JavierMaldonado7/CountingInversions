#Counting Inversion Algorithm
#Javier Maldonado Rivera
#CIIC4025-066

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)

def quickSort(arr, low, high):

    if len(arr) == 1:

        return arr

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)

        quickSort(arr, pi + 1, high)


def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count



def sort_and_counting(array):

    print(array)

    quickSort(array, 0, len(array) - 1)
    n = getInvCount(array, len(array))
    print(n)
    tup = (array, n)
    print(tup)




arr = [1,20,6,4,5]
sort_and_counting(arr)

