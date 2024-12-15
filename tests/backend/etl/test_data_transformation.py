import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))

import pytest
from app.backend.etl.data_transformation import transform_data

def test_transform_data():
    raw_data = {"base_salary": [50000, 60000], "total_pay": [55000, 65000]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "total_pay" in transformed_data
