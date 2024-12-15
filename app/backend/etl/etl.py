import logging
import psycopg2
from ..models.data_transformation import transform_data, PayrollData, SessionLocal

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

def extract_data():
    try:
        data = extract_nyc_payroll_data(NYC_PAYROLL_API_URL)
        return data
    except Exception as e:
        logger.error("Error extracting data: %s", e)
        return None

def transform_data(data):
    try:
        transformed_data = transform_data(data)
        return transformed_data
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        raise

def load_data(data):
    session = SessionLocal()
    try:
        for item in data:
            payroll_data = PayrollData(
                employee_id=item['employee_id'],
                employee_name=item['employee_name'],
                payroll_year=item['payroll_year'],
                base_salary=item['base_salary'],
                total_ot_pay=item['total_ot_pay'],
                total_other_pay=item['total_other_pay'],
                total_pay=item['total_pay']
            )
            session.add(payroll_data)
        session.commit()
    except Exception as e:
        logger.error("Error loading data into the database: %s", e)
    finally:
        session.close()

def run_etl():
    """
    Trigger the ETL process.
    """
    try:
        conn = connect_to_db()
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
    finally:
        if conn:
            conn.close()
