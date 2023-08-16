def quicksort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot = array[0]
    subarray_smaller = [element for element in array[1:] if element <= pivot]
    subarray_greater = [element for element in array[1:] if element > pivot]
    return quicksort(subarray_smaller) + [pivot] + quicksort(subarray_greater)
