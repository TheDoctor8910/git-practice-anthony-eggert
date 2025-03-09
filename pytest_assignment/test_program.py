import pytest
from program import divide_numbers, reverse_string, get_list_element


def test_divide_numbers():
    assert divide_numbers(10, 3) == 3.33

# Edge case: divide by zero should raise ZeroDivisionError
def test_divide_numbers_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(5, 0)

def test_reverse_string():
    assert reverse_string('aBcDeF') == 'fEdCbA'

# Edge case: reverse_string with non-string argument should raise TypeError
def test_reverse_string_with_int():
    with pytest.raises(TypeError):
        reverse_string(120)

# Corner case: while strings are a list of chars, using reverse_string with a list should still raise TypeError
def test_reverse_string_with_list():
    with pytest.raises(TypeError):
        reverse_string(['a', 'B', 'c', 'D', 'e', 'F'])

def test_get_list_element():
    test_list = [1, 3, 5, 7, 9]
    assert get_list_element(test_list, 2) == test_list[2]

# Corner case: using get_list_element with an index not less than the length of the list should raise IndexError
def test_get_list_element_with_large_index():
    test_list = [1, 3, 5, 7, 9]
    with pytest.raises(IndexError):
        get_list_element(test_list, 5)

# Edge case: using get_list_element with a negative index should always raise IndexError
def test_get_list_element_with_negative_index():
    test_list = [1, 3, 5, 7, 9]
    with pytest.raises(IndexError):
        get_list_element(test_list, -1)