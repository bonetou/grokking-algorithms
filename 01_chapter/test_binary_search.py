from binary_search import binary_search

def test_should_find_correct_index():
    assert binary_search([1,2,3,4,5,6,7,8,9], 8) == 7
    assert binary_search([1,3,2,4,9,6,7,8,5], 8) == 7


def test_should_return_none_when_item_is_not_on_given_list():
    assert binary_search([1,2,3,4,5,6,7,8,9], 10) == None
