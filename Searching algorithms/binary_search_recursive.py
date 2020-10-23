"""
BINARY SEARCH - RECURSIVE
Returns index of x in given array 'arr' if present,
else print message
"""


def binary_search(arr, low, high, x):
    # Base case
    if high >= low:
        mid = (high+low)//2

        # The solution
        if arr[mid] == x:
            print(f"Element is present at index {mid}")

        # If x is smaller, ignore right half.
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # If x is greater, ignore left half.
        else:
            return binary_search(arr, mid + 1, high, x)

    # Reach here if element is not presented in the array
    else:
        print("Element is not presented in the array")


arr = [2, 5, 7, 9, 12, 53, 77]
binary_search(arr, 0, len(arr)-1, 1)
binary_search(arr, 0, len(arr)-1, 2)
binary_search(arr, 0, len(arr)-1, 5)
binary_search(arr, 0, len(arr)-1, 7)
binary_search(arr, 0, len(arr)-1, 9)
binary_search(arr, 0, len(arr)-1, 12)
binary_search(arr, 0, len(arr)-1, 53)
binary_search(arr, 0, len(arr)-1, 77)
binary_search(arr, 0, len(arr)-1, 80)
