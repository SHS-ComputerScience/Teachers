# Insertion Sort Algorithm

def insertion_sort(array):

    for i in range(1, len(array)):
        value = array[i]
        j = i - 1

        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = value

    return array

insertion_sort([5, 2, 1, 25, 4])
