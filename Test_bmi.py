import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(weight=70, height=1.75)
    assert result == 0  # Normal Weight

def test_bmi_over_weight():
    result = bmi.calculate_bmi(weight=90, height=1.75)
    assert result == 1  # Over Weight

def test_bmi_under_weight():
    result = bmi.calculate_bmi(weight=50, height=1.75)
    assert result == -1  # Under Weight
