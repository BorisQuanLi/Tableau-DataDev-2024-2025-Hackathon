# ...existing code...
"""
Transforms the input data by applying a series of transformations.

Args:
    data (list of dict): The input data to be transformed. Each element in the list is a dictionary representing a record.

Returns:
    list of dict: The transformed data where all string values in each record are converted to uppercase.
"""

def transform_raw_data(data):
    # Example transformation: Convert all string values to uppercase
    transformed_data = []
    for record in data:
        transformed_record = {key: value.upper() if isinstance(value, str) else value for key, value in record.items()}
        transformed_data.append(transformed_record)
    return transformed_data

def transform_data(data):
    # Apply the transformation
    return transform_raw_data(data)

# Example usage
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

# Apply the transformation
transformed_data = transform_data(data)
print(transformed_data)