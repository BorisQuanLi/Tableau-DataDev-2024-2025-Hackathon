import logging
import requests
from tableauhyperapi import HyperProcess, Connection, Telemetry, SqlType, TableDefinition, Inserter, CreateMode
import os

def extract_data():
    try:
        response = requests.get("https://data.cityofnewyork.us/resource/k397-673e.json")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to extract data: {e}")
        raise

def transform_data(data):
    # Implement any necessary data transformations here
    return data

def load_data(data):
    try:
        with HyperProcess(telemetry=Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:
            connection = Connection(endpoint=hyper.endpoint, database="data.hyper", create_mode=CreateMode.CREATE_AND_REPLACE)
            
            # Define tables
            employees_table = TableDefinition(table_name="Employees", columns=[
                ("employee_id", SqlType.text()),
                ("name", SqlType.text()),
                ("title", SqlType.text()),
                ("department_id", SqlType.text())
            ])
            departments_table = TableDefinition(table_name="Departments", columns=[
                ("department_id", SqlType.text()),
                ("department_name", SqlType.text())
            ])
            payroll_table = TableDefinition(table_name="Payroll", columns=[
                ("payroll_id", SqlType.text()),
                ("employee_id", SqlType.text()),
                ("fiscal_year", SqlType.text()),
                ("base_salary", SqlType.double()),
                ("overtime_pay", SqlType.double()),
                ("total_pay", SqlType.double())
            ])
            
            # Create tables
            connection.catalog.create_table(employees_table)
            connection.catalog.create_table(departments_table)
            connection.catalog.create_table(payroll_table)
            
            # Insert data
            with Inserter(connection, employees_table) as inserter:
                for record in data:
                    inserter.add_row([
                        record.get("employee_id"),
                        record.get("name"),
                        record.get("title"),
                        record.get("department_id")
                    ])
                inserter.execute()
            
            with Inserter(connection, departments_table) as inserter:
                for record in data:
                    inserter.add_row([
                        record.get("department_id"),
                        record.get("department_name")
                    ])
                inserter.execute()
            
            with Inserter(connection, payroll_table) as inserter:
                for record in data:
                    inserter.add_row([
                        record.get("payroll_id"),
                        record.get("employee_id"),
                        record.get("fiscal_year"),
                        record.get("base_salary"),
                        record.get("overtime_pay"),
                        record.get("total_pay")
                    ])
                inserter.execute()
            
            connection.close()
        
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise

def run_etl():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)
