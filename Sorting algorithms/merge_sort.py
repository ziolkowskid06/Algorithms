"""
MERGE SORT
Keeps splitting the list by 2 until it only has singular elements.
Adjacent elements become sorted pairs, then sorted pairs are merged and sorted with other pairs.
The process continues until we get a sorted list with all the elements of the unsorted input list.
"""


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Check which value from the the start of each list is smaller.
            # If the item at the begginng of the left list is smaller,
            # add it to the sorted list.
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smallet,
            # add it to the sorted list.
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # When the left list is done, add elements from the right list.
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # When the right list is done, add elements from the left list.
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(arr):
    # Return if the list has one element only.
    if len(arr) <= 1:
        return arr
    # Find midpoint
    mid = len(arr)//2
    # Sort and merge each half.
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])
    # Merge the sorted list into a new one.
    return merge(left_list, right_list)


# Verification
array = [100, 20, 1, 43, 66, 22, 19, 42, 20]
array = merge_sort(array)
print(array)
