"""
QUICK SORT
It partitions the list around a pivot element, sorting values around the pivot.
"""


def q_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr.pop()
    left = list(filter(lambda x: x <= pivot, arr))
    right = list(filter(lambda x: x > pivot, arr))

    return q_sort(left) + [pivot] + q_sort(right)


array = [10, 9, 6, 2, 6, 2, 4, 3, 1]
array = q_sort(array)
print(array)
