import pytest
from app.backend.models.data_transformation import transform_data

def test_transform_data():
    raw_data = {"base_salary": [50000, 60000], "total_pay": [55000, 65000]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "total_pay" in transformed_data

def test_transform_data_with_bonus():
    raw_data = {"base_salary": [50000, 60000], "bonus": [5000, 6000]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "bonus" in transformed_data

def test_transform_data_with_overtime():
    raw_data = {"base_salary": [50000, 60000], "overtime": [2000, 3000]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "overtime" in transformed_data

def test_transform_data_with_deductions():
    raw_data = {"base_salary": [50000, 60000], "deductions": [1000, 1500]}
    transformed_data = transform_data(raw_data)
    assert "base_salary" in transformed_data
    assert "deductions" in transformed_data
