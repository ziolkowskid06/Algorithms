"""
JUMP SEARCH
Jump ahead by fixed steps.
Once the interval is known, performs linear search operation. 
"""

import math

def jump_search(arr, search):
    # Set a lower bound
    lower_bound = 0
    # Calculate steps
    step = int(math.sqrt(len(arr)))
    # Perform jump search to detect interval, where element exists.
    for i in range(0, len(arr), step):
        # Return index of the element searched
        if arr[i] == search:
            return i
        # Jump, marking lower bound.
        elif arr[i] < search:
            lower_bound = i
        # Stop jumping, when number in the list is higher then number searched    
        else:
            break
    # Assign lower bound.
    index_number = lower_bound
    # Perform linear search.
    for j in arr[lower_bound:]:
        # Element is found.
        if j == search:
            return index_number
        # Keep increasing index until the solution
        index_number += 1
    # If the element not exist
    return "Not found"


# Validation
array = [i for i in range(0, 65, 4)]
index = jump_search(array, 32)
print(f"Element found at index {index}")
