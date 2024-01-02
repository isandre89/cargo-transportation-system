import os
import random
from datetime import datetime


def validate_and_convert_date(date_string):
    try:
        date_object = datetime.strptime(date_string, "%d/%m/%Y")
        current_date = datetime.now().date()

        if date_object.date() > current_date:
            print("Error: Provided date is greater than the current date.")
            return None

        return date_object
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")
        return None


def validate_and_convert_integer(integer_string):
    if (
        integer_string is not None
        and len(integer_string) > 0
        and integer_string.isdigit()
    ):
        return int(integer_string)
    else:
        print("Invalid value. Please use integers.")


def validate_and_convert_float(float_string):
    try:
        float_value = float(float_string)
        return float_value
    except ValueError:
        print("Invalid value. Please use valid float numbers.")
        return None


def validate_and_convert_location(location_string):
    if location_string is not None and len(location_string) >= 3:
        return location_string
    else:
        print("Invalid location. Please type in at least 3 characters.")


def clear_console():
    # Clear console screen
    os.system("cls" if os.name == "nt" else "clear")


def get_random_cost(from_value=5, to_value=150):
    return round(random.uniform(from_value, to_value), 2)
