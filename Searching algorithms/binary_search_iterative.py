"""
BINARY SEARCH - ITERATIVE
Returns index of x in given array 'arr' if present,
else print message
"""


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high+low)//2

        # If x is greater, ignore left half.
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half.
        elif arr[mid] > x:
            high = mid - 1
        # The solution
        else:
            return mid
    # Reach here if element is not presented in the array
        mid = -1

    # Print result
    if mid != -1:
        print(f"Element is present at index {mid}")
    else:
        return "Element is not present in the array"


# Results
print(binary_search([2, 5, 7, 9, 12, 53, 77], 2))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 5))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 7))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 9))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 12))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 53))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 77))
print(binary_search([2, 5, 7, 9, 12, 53, 77], 1))
