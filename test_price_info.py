from price_info import cost_of_fruits, total_cost_shopping


def test_cost_of_fruits():
    expected_value = 6.00
    result = cost_of_fruits('apple', 5)

    if result == expected_value:
        print("test_cost_of_fruits PASSED")



def test_total_cost_shopping():
    expected_value = 46.75
    result = total_cost_shopping()

    assert (result == expected_value)


if __name__ == "__main__":
    test_cost_of_fruits()
    test_total_cost_shopping()
