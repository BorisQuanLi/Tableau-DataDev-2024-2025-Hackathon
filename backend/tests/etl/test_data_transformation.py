import pytest
from backend.etl.data_transformation import transform_data

def test_transform_data():
    raw_data = [
        {
            'EmployeeID': '123',
            'EmployeeName': 'John Doe',
            'PayrollYear': '2021',
            'BaseSalary': '50000',
            'TotalOTPay': '5000',
            'TotalOtherPay': '2000',
            'TotalPay': '57000'
        }
    ]
    expected_data = [
        {
            'employee_id': '123',
            'employee_name': 'John Doe',
            'payroll_year': '2021',
            'base_salary': 50000.0,
            'total_ot_pay': 5000.0,
            'total_other_pay': 2000.0,
            'total_pay': 57000.0
        }
    ]
    transformed_data = transform_data(raw_data)
    assert transformed_data == expected_data
