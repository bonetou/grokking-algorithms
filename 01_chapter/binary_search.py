from typing import Any


def binary_search(ordered_list_of_items: list, item: Any) -> int:
    low = 0
    high = len(ordered_list_of_items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = ordered_list_of_items[mid]

        if guess == item:
            return mid
        
        elif guess > item:
            high = mid - 1

        elif guess < item:
            low = mid + 1
        
    return -1
''