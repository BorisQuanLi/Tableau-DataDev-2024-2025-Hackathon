import os
import psycopg2
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
import logging

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Print environment variables to verify they are loaded correctly
logger.debug("DB_NAME: %s", os.getenv("POSTGRES_DB"))
logger.debug("DB_USER: %s", os.getenv("POSTGRES_USER"))
logger.debug("DB_PASSWORD: %s", os.getenv("POSTGRES_PASSWORD"))
logger.debug("DB_HOST: %s", os.getenv("POSTGRES_HOST"))

# Construct the database URI using environment variables
db_uri = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"

# Ensure you are using a SQLAlchemy engine or connection
engine = sqlalchemy.create_engine(db_uri)
connection = engine.connect()

def get_db_connection():
    logger.debug("Getting database connection")
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST")
    )
    return conn

def get_connection():
    return get_db_connection()

def create_payroll_data_table():
    logger.debug("Creating payroll_data table if not exists")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payroll_data (
        id SERIAL PRIMARY KEY,
        base_salary NUMERIC,
        total_pay NUMERIC,
        employee_name VARCHAR(255)
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    logger.debug("Table created and connection closed")

def fetch_data(query: str):
    logger.debug("Fetching data with query: %s", query)
    create_payroll_data_table()  # Ensure the table exists before fetching data
    # Ensure the connection is open
    global connection
    if connection.closed:
        connection = engine.connect()
    df = pd.read_sql(query, connection)
    connection.close()
    logger.debug("Data fetched and connection closed")
    return df
