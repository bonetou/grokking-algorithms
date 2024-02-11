import random
from binary_search import binary_search

def test_should_find_correct_index():
    list_of_ordered_items = list(range(0,100))
    item_to_search = random.choice(list_of_ordered_items)
    index_where_item_is = list_of_ordered_items.index(item_to_search)

    assert binary_search(list_of_ordered_items, item_to_search) == index_where_item_is


def test_should_return_none_when_item_is_not_on_given_list():
    assert binary_search([1,2,3,4,5,6,7,8,9], 10) == -1
