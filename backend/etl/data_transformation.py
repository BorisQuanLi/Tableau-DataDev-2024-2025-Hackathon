def transform_data(data):
    """
    Transform the extracted NYC Payroll data.

    Args:
        data (list of dict): The extracted data.

    Returns:
        list of dict: The transformed data.
    """
    transformed_data = []
    for row in data:
        transformed_row = {
            'employee_id': row['EmployeeID'],
            'employee_name': row['EmployeeName'],
            'payroll_year': row['PayrollYear'],
            'base_salary': float(row['BaseSalary']),
            'total_ot_pay': float(row['TotalOTPay']),
            'total_other_pay': float(row['TotalOtherPay']),
            'total_pay': float(row['TotalPay'])
        }
        transformed_data.append(transformed_row)
    return transformed_data
