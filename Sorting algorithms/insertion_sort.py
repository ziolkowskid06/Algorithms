"""
INSERTION SORT
Segments list into sorted and unsorted parts.
Iterates over the unsorted segment, and inserts the element being viewed into
the correct position of the sorted list.
"""


def insertion_sort(arr):
    # Index of the unsorted list.
    for index in range(1, len(arr)):
        # Take each element from the unsorted list.
        item_to_insert = arr[index]
        # Starting from the end of the sorted list, move forward each element
        # if is higher then element to insert.
        while index > 0 and arr[index-1] >= item_to_insert:
            arr[index] = arr[index-1]
            index -= 1
        # Insert element in correct position (gap) of sorted list
        arr[index] = item_to_insert


# Validation
array = [9, 4, 7, 1, 5, 7, 3, 8]
insertion_sort(array)
print(array)
