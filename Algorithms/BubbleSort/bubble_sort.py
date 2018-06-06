# Bubble Sort Algorithm

# -------------------------------
# Version 1
# -------------------------------

num_items = len(array)
for i in range(num_items - 2):
	for j in range(num_items - i - 2):
		if array[j] > array[j+1]:
			temp = array[j]
			array[j] = array[j+1]
			array[j+1] = temp


# -------------------------------
# Version 2
# -------------------------------

num_items = len(array)
swapped = True

while num_items > 0 and swapped:
	swapped = False
	num_items = num_items - 1

	for i in range(num_items):
		if array[i] > array[i+1]:
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp
			swapped = True
