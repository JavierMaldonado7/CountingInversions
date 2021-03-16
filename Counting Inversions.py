#Counting Inversion Algorithm
#Javier Maldonado Rivera
#CIIC4025-066

def homieCheckFront(array,current,index):
    if(array[current] < array[current + index]):

        if (current + index + 1 == len(array)):
            return True

        else:
            homieCheckFront(array, current, index + 1)

    else:

        return current + index

def homieCheckBack(array,current,index):
    if (array[current] > array[current - index]):

        if(current - index + 1 < 0):

            return True

        else:

            homieCheckBack(array,current,index+1)

    else:

        return current - index


def homieSwap(array,current,index):
    if(homieCheckBack(array,current)):
        holdup = array[current+index]
        homie = array[current]
        array[current] = holdup
        array[current+1] = homie


def homieSort(array):

    inversion = 0

    l = len(array) - 1

    middle = l//2
    if(homieCheckBack(array,middle,1).isinstance(int)):
        homieSwap(ar)







# sort_and_counting(array):
