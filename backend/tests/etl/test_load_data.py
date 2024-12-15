import pytest
from unittest.mock import MagicMock
from backend.etl.load_data import load_data

def test_load_data():
    mock_conn = MagicMock()
    data = [
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
    load_data(mock_conn, data)
    mock_conn.cursor().execute.assert_called_once_with(
        "INSERT INTO your_table_name (employee_id, employee_name, payroll_year, base_salary, total_ot_pay, total_other_pay, total_pay) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        ('123', 'John Doe', '2021', 50000.0, 5000.0, 2000.0, 57000.0)
    )
    mock_conn.commit.assert_called_once()
    mock_conn.cursor().close.assert_called_once()
