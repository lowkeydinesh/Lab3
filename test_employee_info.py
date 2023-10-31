# test_employee_info.py

from employee_info import (
    get_employees_by_age_range,
    calculate_average_salary,
    employee_data,
    get_employees_by_dept,

)

def test_get_employees_by_age_range():
    # Test case with age range 25 to 35
    result = get_employees_by_age_range(24, 36)
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]

    # Check if the result matches the expected result
    assert result == expected_result

def test_calculate_average_salary():
    # Calculate the expected average salary manually
    total_salary = sum(item["salary"] for item in employee_data)
    expected_result = total_salary / len(employee_data) if len(employee_data) > 0 else 0

    # Call the function
    result = calculate_average_salary()

    # Assert that the result matches the expected value
    assert result == expected_result

def test_get_employees_by_dept():
    # Choose a department from your employee_data
    department = "Sales"

    # Call the function to get employees in the chosen department
    result = get_employees_by_dept(department)

    # Filter the expected result manually based on the chosen department
    expected_result = [item for item in employee_data if item["department"] == department]

    # Assert that the result matches the expected value
    assert result == expected_result









