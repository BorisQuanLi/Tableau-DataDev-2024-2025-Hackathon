def load_data(conn, data):
    """
    Load data into the PostgreSQL database.

    Args:
        conn: The database connection object.
        data (list of dict): The transformed data.
    """
    cursor = conn.cursor()
    for row in data:
        cursor.execute(
            "INSERT INTO your_table_name (employee_id, employee_name, payroll_year, base_salary, total_ot_pay, total_other_pay, total_pay) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (row['employee_id'], row['employee_name'], row['payroll_year'], row['base_salary'], row['total_ot_pay'], row['total_other_pay'], row['total_pay'])
        )
    conn.commit()
    cursor.close()
