# Bubble Sort Algorithm

def bubble_sort(array):

	number_of_passes = len(array) - 1

	for i in range(number_of_passes):
		for j in range(number_of_passes - i):

			if array[j] > array[j+1]:
				array[j], array[j + 1] = array[j + 1], array[j]

	return array
