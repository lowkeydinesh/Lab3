import Lab3 as check

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def test_ascending_order():

   arr = [64, 34, 25, 12, 22, 11, 90]

   result = check.bubble_sort(arr,SORT_ASCENDING)
   expected_result = [11, 12, 22, 25, 34, 64, 90]

   assert result == expected_result


def test_descending_order():
    arr = [64, 34, 25, 12, 22, 11, 90]

    result = check.bubble_sort(arr, SORT_DESCENDING)
    expected_result = [90, 64, 34, 25, 22, 12, 11]

    assert result == expected_result

def test_large_number():
    arr = [64, 34, 25, 12, 22, 11, 90, 5, 6, 7]

    result = check.bubble_sort(arr, SORT_DESCENDING)
    expected_result = 1

    assert result == expected_result
def test_no_number():

    empty_array = []

    result = check.bubble_sort(empty_array, SORT_ASCENDING)
    expected_result = 0

    assert result == expected_result
def test_not_number():
    arr = [64, 34, 25, "abc", 22, 11, 90]

    result = check.bubble_sort(arr, SORT_DESCENDING)
    expected_result = 2

    assert result == expected_result