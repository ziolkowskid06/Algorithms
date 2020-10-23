"""
INSERTION SORT
Sorting custom objects.
Sorting points according to x-coordinate.
Comparison method - lambda function take an argument.
"""


class Point:
    """Defines point in cartesian coordinates"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Returns point"""
        return str.format("({}, {})", self.x, self.y)


def insertion_sort(arr, compare_function):
    # Index of the unsorted list.
    for index in range(1, len(arr)):
        # Take each element from the unsorted list.
        item_to_insert = arr[index]
        # Starting from the end of the sorted list, move forward each element
        # if is higher then element to insert.
        while index > 0 and compare_function(arr[index-1], item_to_insert):
            arr[index] = arr[index-1]
            index -= 1
        # Insert element in correct position (gap) of sorted list
        arr[index] = item_to_insert


# Test the program.
A = Point(7, 8)
B = Point(5, 3)
C = Point(7, 9)
D = Point(3, 5)
E = Point(1, 3)

array = [A, B, C, D, E]

# Sorts by the x coordinate ascending.
insertion_sort(array, lambda a, b: a.x > b.x)

# Print result
for point in array:
    print(point)
