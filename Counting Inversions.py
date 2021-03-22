#Counting Inversion Algorithm
#Javier Maldonado Rivera
#CIIC4025-066


def mSort(arr):

    temp_arr = [0] * len(arr)
    return mergeSort(arr, temp_arr, 0, len(arr) - 1)

def mergeSort(arr, temp_arr, left, right):

    inversion = 0

    if left < right:

        middle = (left + right) // 2

        inversion = inversion + mergeSort(arr, temp_arr,left, middle)[1]

        inversion = inversion +  mergeSort(arr, temp_arr,middle + 1, right)[1]


        inversion = inversion + merge(arr, temp_arr, left, middle, right)

    TUP = (temp_arr,inversion)

    return TUP


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inversion = 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:

            temp_arr[k] = arr[j]
            inversion += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1


    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for a in range(left, right + 1):
        arr[a] = temp_arr[a]

    return inversion

def sort_and_counting(arr):

    return (mSort(arr))



