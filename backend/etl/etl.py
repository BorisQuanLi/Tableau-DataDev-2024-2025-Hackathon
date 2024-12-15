import logging
from .nyc_payroll_extraction import extract_nyc_payroll_data, NYC_PAYROLL_API_URL
from .db_connection import connect_to_db
from backend.models.data_transformation import transform_data
from .load_data import load_data

def run_etl():
    """
    Trigger the ETL process.
    """
    conn = connect_to_db()
    data = extract_nyc_payroll_data()
    transformed_data = transform_data(data)
    load_data(conn, transformed_data)
    conn.close()
