import pytest
from app.backend.etl.etl import extract_data, load_data

def test_extract_data():
    data = extract_data()
    assert data is not None

def test_load_data():
    data = {"base_salary": [50000, 60000], "total_pay": [55000, 65000]}
    load_data(data)
    # Add assertions to verify data loading if possible

def test_get_connection(db_connection):
    assert db_connection is not None

# Ensure the import paths are correct and remove any __pycache__ or .pyc files.