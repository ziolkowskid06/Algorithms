"""
SELECTION SORT
Segments the list into two parts: sorted and unsorted.
Removes the smallest element of the unsorted segment of the list and
appends it to the sorted segment.
"""


def selection_sort(arr):
    """Leftmost part of the list will be sorted"""
    # The value i corresponds to how many elements were sorted
    for i in range(len(arr)):
        # Assume the first element is the smallest
        lowest_value_index = i
        # Iterate over unsorted elements
        for j in range(i + 1, len(arr)):
            # Find the lowest value
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        # Swap elements in the array
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]


# Validation
arr = [12, 123, 1, 3, 5, 13, 2, 12]
selection_sort(arr)
print(arr)
