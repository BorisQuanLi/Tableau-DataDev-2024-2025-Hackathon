import pytest
from app.backend.models.data_transformation import transform_data

def test_transform_data():
    raw_data = {"base_salary": [50000, 60000], "total_pay": [55000, 65000]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "total_pay" in transformed_data
