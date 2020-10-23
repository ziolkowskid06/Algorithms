"""

"""

def heapify(arr, heap_size, root_index):
    """Assumes part of array is already sorted"""
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2*root_index) + 1
    right_child = (2*root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)

def heap_sort(arr):
    length = len(arr)
    # Create a Max Heap from the list.
    for i in range(length, -1, -1):
        heapify(arr, length, i)

    # Move the root of the max heap to the end of the list.
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i , 0)

array = [44, 21, 2, 10, 32, 45, 10]
heap_sort(array)
print(array)

                                                
