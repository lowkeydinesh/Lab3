import employee_info

def test_get_employees_by_age_range():

    test_result = [{'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000},
                   {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]
    result = employee_info.get_employees_by_age_range(30, 40)
    assert (result == test_result)

def test_calculate_average_salary():

    test_result = 60166.666666666664
    result = employee_info.calculate_average_salary()
    assert (result == test_result)

def test_get_employees_by_dept():

    test_result = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000},
                   {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    result = employee_info.get_employees_by_dept("Sales")
    assert (result == test_result)