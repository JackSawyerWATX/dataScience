def reverse_in_place(arr):
	"""Reverse the list `arr` in place using a two-pointer algorithm."""
	i, j = 0, len(arr) - 1
	while i < j:
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1


def reversed_copy(arr):
	"""Return a new list which is the reverse of `arr`."""
	return arr[::-1]


if __name__ == "__main__":
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print("original:", array)
	print("reversed copy:", reversed_copy(array))
	reverse_in_place(array)
	print("after in-place reverse:", array)
