import pytest
import random
from selection_sort import selection_sort, find_smallest


@pytest.fixture
def random_list() -> list:
    return random.sample(range(1, 100), 20)


def test_should_sort_array_from_smallest_to_largest(random_list):
    assert selection_sort(random_list) == sorted(random_list)


def test_should_find_smallest_item_index(random_list):
    smallest_item = min(random_list)
    smallest_index = random_list.index(smallest_item)
    assert find_smallest(random_list) == (smallest_index, smallest_item)
