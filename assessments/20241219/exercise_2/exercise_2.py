# Python Data Engineering Coding Exercises

#Exercise 2: Data Schema Validator

import re


'''Sample Schema JSON'''

schema = {
        "tables": [
            {
                "name": "customers",
                "columns": [
                    {
                    "name": "customer_id",
                    "type": "string",
                    "required": True,
                    "validation": {
                        "pattern": "^CUS[0-9]{6}$"
                    }
                    },
                    {
                    "name": "purchase_amount",
                    "type": "decimal",
                    "required": True,
                    "validation": {
                        "min": 0,
                        "max": 1000000
                    }
                    }
                ]
            }
        ]
    }


''' Sample data to validate'''

input_data = {
    "customer_id": "CUS123456",
    "purchase_amount": 2500
}


''' Function that extracts column details from the schema file:
        Use lambda functions to transform complex column definitions
        Create a mapping of table names to their column specifications
'''
def extract_column_details(schema):
    columns = lambda table: {table['name'] : [column['name'] for column in table['columns']]}
    return list(map(columns, schema['tables']))


'''Validation function that:
        Filters required columns using filter() and lambda
        Validates data types and constraints
        Returns validation errors in a structured format
'''
def validation(schema,data):
    errors=[]
    for table in schema['tables']:
        table_name = table['name']
        for column in filter(lambda col: col['required'], table['columns']):
            column_name = column['name'] 
            validation = column['validation']

            if column_name not in data:
                 errors.append(f"Missing column name : {column_name}")
                 continue

            value = data[column_name]

            if "pattern" in validation:
                pattern = validation["pattern"]
                if not re.match(pattern, str(value)):
                    errors.append({"message": f"Invalid format for column: {column_name}. Expected pattern: {pattern}", "severity": 1, "table": table_name, "column": column_name})
            if "min" in validation:
                min_value = validation["min"]
                if value < min_value:
                    errors.append({"message": f"Value for {column_name} is below the minimum allowed: {min_value}", "severity": 2, "table": table_name, "column": column_name})
            if "max" in validation:
                max_value = validation["max"]
                if value > max_value:
                    errors.append({"message": f"Value for {column_name} exceeds the maximum allowed: {max_value}", "severity": 2, "table": table_name, "column": column_name})

    return errors


''' Function that sorts validation errors by:
        Error severity
        Table name
        Column name
'''
def sort_errors(errors):
    return sorted(errors, key=lambda e: (e["severity"], e["table"], e["column"]))


''' Wrong data to validate '''
input_data = {
    "customer_id": "CUS1234",
    "purchase_amount": -3
}
errors = validation(schema, input_data)
sorted_errors = sort_errors(errors)

''' Print results'''
for error in sorted_errors:
    print(error)