import json
import time

""" Method verifies JSON format input data """


def verifying_input_json(path):  # Argument is the path to the JSON file.
    with open(path, "r") as file:  # Opening a file in read mode.
        data = json.load(file)  # Loading data from a file into a variable.

    # Checking whether the 'Resource' field in the JSON data contains the '*' character.
    if data.get('Resource', '') == '*':
        return False
    else:
        return True


# Display of the result
print(verifying_input_json("data.json"))
time.sleep(6000)