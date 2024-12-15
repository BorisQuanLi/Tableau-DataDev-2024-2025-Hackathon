import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Print environment variables to verify they are loaded correctly
print("DB_NAME:", os.getenv("POSTGRES_DB"))
print("DB_USER:", os.getenv("POSTGRES_USER"))
print("DB_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("DB_HOST:", os.getenv("POSTGRES_HOST"))

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST")
    )
    return conn

def fetch_data(query: str):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
