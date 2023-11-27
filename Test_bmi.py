import Lab2.bmi as bmi

def test_bmi_normal_weight():
   result = bmi.calculate_bmi(weight=57,height=1.73)
   expected_result = 0

   assert result == expected_result


def test_bmi_over_weight():
    result = bmi.calculate_bmi(weight=100, height=1.53)

    expected_result = 1

    assert result == expected_result

def test_bmi_under_weight():
    result = bmi.calculate_bmi(weight=37, height=1.73)

    expected_result = -1

    assert result == expected_result
