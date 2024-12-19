# Python Data Engineering Coding Exercises

#Exercise 2: Data Schema Validator


import json
from jsonschema import validate


# Describe expected JSON form.
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


# Convert json to python object
my_json = json.loads('{"name": "customer_id", "type": "abc", "required": "True", "validation": 3}')

# Validate will raise exception if given json is not what is described in schema.
validate(instance=my_json, schema=schema)

# print for debug
print(my_json)

import json
def validate(filename):
    with open(filename) as file:
        try:
            data = json.load(file) # put JSON-data to a variable
            print("Valid JSON")    # in case json is valid
            return data
        except json.decoder.JSONDecodeError:
            print("Invalid JSON")  # in case json is invalid


  