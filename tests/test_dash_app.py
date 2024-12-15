import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../path_utils')))
from path_utils import add_project_root_to_sys_path
add_project_root_to_sys_path()

import pytest
from unittest.mock import patch
import pandas as pd
from app.dash_app import fetch_data, app, create_payroll_data_table
from app.backend.utils.db_utils import get_db_connection

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

@patch('app.backend.utils.db_utils.fetch_data')
def test_fetch_data(mock_fetch_data):
    mock_fetch_data.return_value = pd.DataFrame({
        "base_salary": [50000, 60000],
        "total_pay": [55000, 65000],
        "employee_name": ["John Doe", "Jane Smith"]
    })
    df = fetch_data("SELECT * FROM payroll_data")
    assert not df.empty

def test_dash_app_layout():
    # Check if the app layout contains the expected components
    assert 'Citywide Payroll Data Visualization' in app.layout.children[0].children
    assert app.layout.children[1].id == 'example-graph'
