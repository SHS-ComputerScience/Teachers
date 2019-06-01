# Binary Search Algorithm

def binary_search(sortedArray, value):

	low = 0
	high = len(sortedArray) - 1

	while low <= high:
		mid = (low + high) // 2

		if sortedArray[mid] > value:
			high = mid - 1
		elif sortedArray[mid] < value:
			low = mid + 1
		else:
			return True		# value found

	return False			# value not
