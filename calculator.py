from helper_functions import *

allowed_operations = ["+", "-", "*", "/"]
number1 = ""
number2 = ""
attempt = 0
operation = ""

print("Enter two numbers")
while not (check_if_numeric(number1)):
    if attempt > 0:
        print("That's not a valid number")
    attempt += 1
    number1 = input("Number 1: ")
number1 = int(number1)

attempt = 0

while not (check_if_numeric(number2)):
    if attempt > 0:
        print("That's not a valid number")
    attempt += 1
    number2 = input("Number 2: ")
number2 = int(number2)

attempt = 0

while operation not in allowed_operations:
    if attempt > 0:
        print("That's not a valid operation")
    attempt += 1
    print(
        f"Enter the operation that you want to perform. '+' to add, '-' to subtract,"
        "'*' to multiply, and '/' to divide"
    )
    operation = input("")

del attempt

if number2 == 0 and operation == "/":
    print("Division by zero is not possible")
else:
    print(f"{number1} {operation} {number2} = {result(number1,operation,number2)}")
