import price_info

def test_total_cost_shipping():
    test_result = 46.75
    result = price_info.total_cost_shopping()
    assert(result == test_result)
def test_cost_of_fruit():
    testfruit = 'apple'
    testquantity = 10
    test_result = 12.0
    result = price_info.cost_of_fruits(testfruit, testquantity)
    assert (result == test_result)