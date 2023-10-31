# Test_Lab3.py

import Lab3

def test_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_result = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == expected_result

def test_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_result = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert result == expected_result

def test_empty_array():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 0)

def test_large_array():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 43, 56, 78, 9, 8, 7, 6, 5]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 1)

def test_non_integer_values():
    input_arr = [64, "abc", 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 2)