from typing import Any, Union


def binary_search(list_of_items: list, item: Any) -> Union[int, None]:
    sorted_list_of_items = sorted(list_of_items)
    low = 0
    high = len(sorted_list_of_items) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = sorted_list_of_items[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1

        if guess < item:
            low = mid + 1
        
    return None
