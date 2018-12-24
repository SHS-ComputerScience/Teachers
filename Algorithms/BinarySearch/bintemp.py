def binary_search(array, value):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] > value:
            high = mid
        elif array[mid] < value:
            low = mid + 1
        else:
            return mid
    
    return -1


# test
test_array = 'abcdefghij'
val = 'x'
index = binary_search(test_array, val)
if index != -1:
    print(val, 'found at index', index)
else:
    print(val, 'not found in array')