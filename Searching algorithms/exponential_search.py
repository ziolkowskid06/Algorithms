"""
EXPONENTIAL SEARCH
Determines the range where the element is likely to be.
Then Binary Search is used to find the index.
"""


def binary_search(ar, low, high, nmb_searched):
    while (low <= high):
        # Calculate middle element each iteration.
        mid = (low+high)//2
        if ar[mid] == nmb_searched:
            # Element found
            return f"Element is present at index {mid}"
        else:
            if nmb_searched < ar[mid]:
                # Search left half.
                high = mid - 1
            else:
                # Search right half.
                low = mid + 1
    # Element is not in the array.
    return "Element not found"


def exponential_search(arr, number_searched):
    if arr[0] == number_searched:
        return "Element is present at index 0"
    index = 1
    while (index < len(arr)) and (arr[index] <= number_searched):
        index *= 2
    # Call binary search for the found range.
    return binary_search(arr, index//2, min(index, len(arr)-1), number_searched)


arr = [2, 5, 7, 9, 10, 12, 53, 77]
number = exponential_search(arr, 77)
print(number)
