from copy import deepcopy
from typing import Any, Union


def selection_sort(array: list[Any]) -> list[Any]:
    array = deepcopy(array)
    sorted_array = []
    for _ in range(len(array)):
        smallest_item_index, smallest_item = find_smallest(array)
        sorted_array.append(smallest_item)
        array.pop(smallest_item_index)
    return sorted_array


def find_smallest(array: list[Any]) -> Union[int, Any]:
    smallest_item = array[0]
    smallest_index = 0
    for current_index in range(len(array)):
        current_item = array[current_index]
        if current_item < smallest_item:
            smallest_item = current_item
            smallest_index = current_index
    return smallest_index, smallest_item
