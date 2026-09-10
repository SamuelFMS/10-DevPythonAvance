from datetime import date, datetime


def input_number(message: str, min: int, max: int) -> int:
    try:
        saisie = int(input(message))
        if saisie >= min and saisie <= max:
            return saisie
        else:
            return input_number(message, min, max)
    except ValueError:
        print("Incorrect input. Please enter a number")
        return input_number(message, min, max)

def input_str(message: str, accept_null: bool) -> str:
    saisie = input(message)
    if saisie == "" and not accept_null:
        return input_str(message, accept_null)
    else:
        return saisie

def input_date(message: str) -> date:
    date_input = input(message)
    try:
        date = datetime.strptime(date_input, "%d-%m-%Y")
        return date
    except ValueError:
        print("Incorrect input. Please enter a date (dd-mm-yyyy)")
        return input_date(message)