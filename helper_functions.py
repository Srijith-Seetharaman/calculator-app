def add(number1: int, number2: int) -> int:
    return number1 + number2


def subtract(number1: int, number2: int) -> int:
    return number1 - number2


def multiply(number1: int, number2: int) -> int:
    return number1 * number2


def divide(number1: int, number2: int) -> int:
    return number1 / number2


def check_if_numeric(string: str) -> bool:
    return string.isnumeric()


def result(number1: int, operator: str, number2: int) -> int:
    if operator == "+":
        return add(number1, number2)
    elif operator == "-":
        return subtract(number1, number2)
    elif operator == "*":
        return multiply(number1, number2)
    else:
        if number2 != 0:
            return divide(number1, number2)
