import pytest
from my_test_cases import my_sum

def test_sum_integers():
    assert my_sum([1, 2, 3, 4, 5]) == 15

def test_sum_floats():
    assert my_sum([1.1, 2.2, 3.3]) == 6.6

def test_empty_list():
    assert my_sum([]) == 0

def test_list_of_strings():
    assert my_sum(['a', 'b', 'c']) == 'abc'

def test_single_integer():
    assert my_sum(5) == 5

def test_single_float():
    assert my_sum(5.5) == 5.5

def test_single_string():
    assert my_sum('abc') == 'abc'

def test_mixed_list():
    with pytest.raises(TypeError):
        my_sum([1, 'a'])