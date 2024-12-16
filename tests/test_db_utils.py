import pytest
from unittest.mock import patch
import pandas as pd
from app.backend.utils.db_utils import create_payroll_data_table, fetch_data, get_db_connection

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    create_payroll_data_table()

def test_create_payroll_data_table():
    create_payroll_data_table()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT to_regclass('public.payroll_data')")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    assert result[0] == 'payroll_data'

@patch('app.backend.utils.db_utils.fetch_data', autospec=True)
def test_fetch_data(mock_fetch_data):
    mock_fetch_data.return_value = pd.DataFrame({
        "base_salary": [50000, 60000],
        "total_pay": [55000, 65000],
        "employee_name": ["John Doe", "Jane Smith"]
    })
    df = fetch_data("SELECT * FROM payroll_data")
    assert len(df) == 2
    assert "base_salary" in df.columns
    assert "total_pay" in df.columns
    assert "employee_name" in df.columns
