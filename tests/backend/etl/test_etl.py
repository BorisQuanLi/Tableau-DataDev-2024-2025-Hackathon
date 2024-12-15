import pytest
from app.backend.etl.etl import extract_data, load_data

def test_extract_data():
    data = extract_data()
    assert data is not None

def test_load_data():
    data = {"base_salary": [50000, 60000], "total_pay": [55000, 65000]}
    load_data(data)
    # Add assertions to verify data loading if possible
