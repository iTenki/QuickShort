def sub_sort(array, low, high):
	key = array[low]
	while low < high:
		while low < high and array[high] >= key:
			high -= 1
		while low < high and array[high] < key:
			array[low] = array[high]
			low += 1
			array[high] = array[low]
	array[low] = key
	return low

def quick_sort1(array, low, high):
	if low < high:
		key_index = sub_sort(array, low, high)
		quick_sort1(array, low, key_index)
		quick_sort1(array, key_index + 1, high)
	return array


'''
Test Example

array1 = [6, 4, 2, 5, 6, 7, 8, 2, 1, 10, 1]
array_sorted = quick_sort1(array1, 0, len(array1) - 1) 
print(array_sorted)
'''