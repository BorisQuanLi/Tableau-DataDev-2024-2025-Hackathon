import pytest
from unittest.mock import patch, MagicMock
from backend.etl.etl import run_etl
from backend.models.data_transformation import transform_data

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

@patch('backend.etl.etl.connect_to_db')
@patch('backend.etl.etl.extract_nyc_payroll_data')
@patch('backend.etl.etl.transform_data')
@patch('backend.etl.etl.load_data')
def test_run_etl(mock_load_data, mock_transform_data, mock_extract_data, mock_connect_db):
    mock_conn = MagicMock()
    mock_connect_db.return_value = mock_conn
    mock_extract_data.return_value = [{'EmployeeID': '123'}]
    mock_transform_data.return_value = [{'employee_id': '123'}]

    run_etl()

    mock_connect_db.assert_called_once()
    mock_extract_data.assert_called_once()
    mock_transform_data.assert_called_once_with([{'EmployeeID': '123'}])
    mock_load_data.assert_called_once_with(mock_conn, [{'employee_id': '123'}])
    mock_conn.close.assert_called_once()
