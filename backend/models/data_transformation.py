def transform_data(data):
    transformed_data = []
    for item in data:
        transformed_item = {
            'employee_id': item['EmployeeID'],
            'employee_name': item['EmployeeName'],
            'payroll_year': item['PayrollYear'],
            'base_salary': float(item['BaseSalary']),
            'total_ot_pay': float(item['TotalOTPay']),
            'total_other_pay': float(item['TotalOtherPay']),
            'total_pay': float(item['TotalPay'])
        }
        transformed_data.append(transformed_item)
    return transformed_data