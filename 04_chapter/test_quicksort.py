from quicksort import quicksort


def test_should_sort_an_array_with_less_than_two_elements():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([2]) == [2]


def test_should_sort_an_array_with_two_or_more_elements():
    assert quicksort([2, 1]) == [1, 2]
    assert quicksort([3, 2, 1]) == [1, 2, 3]
