"""
INTERPOLATION SEARCH
Improvemnt over Binary Search for instances,
where the values in a sorted array are uniformly distributed. 
"""

def interpolation_search(arr, number_searched):
    # Determine bounds
    length = len(arr)
    low = 0               # First index
    high = (length - 1)   # Last index

    while low <= high and number_searched >= arr[low] and number_searched <= arr[high]:
        if low == high:
            if arr[low] == number_searched:
                return low
            return "Element not found"
        # Calculate the position by interpolation.
        position = low + int(((float(high-low)/(arr[high]-arr[low]))*
                              (number_searched-arr[low])))
        # Number is found.
        if arr[position] == number_searched:
            return position
        # Search upper part.
        if arr[position] < number_searched:
            low = position + 1
        # Search lower part.
        else:
            high = position - 1
    # Element does not exist.
    return "Element not found"

# Validation.
arr = [i for i in range(0, 101)]
index = interpolation_search(arr, 33)
print(f"The index of the number is {index}")

