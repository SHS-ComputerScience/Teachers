# Quick Sort Algorithm

from random import choice

def quick_sort(array):
	if len(array) <= 1:
		return array
	else:
		less = []
		more = []
		pivot = choice(array)
		for item in array:
			if item < pivot:
				less.append(item)
			elif item > pivot:
				more.append(item)
		less = quick_sort(less)
		more = quick_sort(more)
		return less + [pivot] * array.count(pivot) + more