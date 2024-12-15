import logging
import psycopg2
from backend.etl.nyc_payroll_extraction import extract_nyc_payroll_data, NYC_PAYROLL_API_URL
from backend.models.data_transformation import transform_data

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="tableau_data_dev",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        return conn
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise

def load_data(conn, data):
    try:
        with conn.cursor() as cursor:
            for item in data:
                cursor.execute(
                    """
                    INSERT INTO payroll_data (employee_id, employee_name, payroll_year, base_salary, total_ot_pay, total_other_pay, total_pay)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (item['employee_id'], item['employee_name'], item['payroll_year'], item['base_salary'], item['total_ot_pay'], item['total_other_pay'], item['total_pay'])
                )
        conn.commit()
    except Exception as e:
        logging.error(f"Error loading data into the database: {e}")
        conn.rollback()
        raise

def run_etl():
    """
    Trigger the ETL process.
    """
    try:
        conn = connect_to_db()
        data = extract_nyc_payroll_data()
        transformed_data = transform_data(data)
        load_data(conn, transformed_data)
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
    finally:
        if conn:
            conn.close()
