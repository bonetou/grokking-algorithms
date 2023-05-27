from typing import Any, Union


def binary_search(ordered_list_of_items: list, item: Any) -> Union[int, None]:
    low = 0
    high = len(ordered_list_of_items) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = ordered_list_of_items[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1

        if guess < item:
            low = mid + 1
        
    return None
