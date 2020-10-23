"""
BUBBLE SORT
Iterates over a list, comparing elements in pairs and swapping them until
the largest element "bubbles up" to the end of the list, and the smallest element
stays at the "bottom"
"""


def bubble_sort(arr):
    swapped = True
    x = 0
    while swapped:
        swapped = False
        x += 1
        # Avoid iteration till last index
        for i in range(len(arr) - x):
            if arr[i] > arr[i + 1]:
                # Swap th elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the flag to True to loop again
                swapped = True


# Verification
array = [8, 4, 3, 1, 4, 7, 2, 1, 5]
bubble_sort(array)
print(array)
