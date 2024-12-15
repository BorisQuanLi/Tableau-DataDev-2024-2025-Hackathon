import pytest
from unittest.mock import patch
import pandas as pd
from app.dash_app import fetch_data, app

@pytest.fixture
def mock_fetch_data():
    with patch('backend.utils.db_utils.fetch_data') as mock:
        mock.return_value = pd.DataFrame({
            "base_salary": [50000, 60000],
            "total_pay": [55000, 65000],
            "employee_name": ["John Doe", "Jane Smith"]
        })
        yield mock

def test_fetch_data(mock_fetch_data):
    df = fetch_data("SELECT * FROM payroll_data")
    assert len(df) == 2
    assert "base_salary" in df.columns
    assert "total_pay" in df.columns
    assert "employee_name" in df.columns

def test_dash_app_layout():
    # Check if the app layout contains the expected components
    assert 'Citywide Payroll Data Visualization' in app.layout.children[0].children
    assert app.layout.children[1].id == 'example-graph'
