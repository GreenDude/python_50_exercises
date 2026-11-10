# Exercise 25: Command-Line Calculator
# Topic: sys
#
# Task:
# Accept two numbers and an operator (+, -, *, /) as command-line arguments and print the result.
#
# Requirements / hints:
# Handle missing/invalid arguments, unknown operators, and division by zero. Use exit codes.
#
# Write your solution below.

import sys

supported_operations = ["+", "-", "*", "/"]
first_number = 0
second_number = 0
operation = ""

arguments = sys.argv

print(arguments)

for arg in arguments:
    if arg in supported_operations:
        operation = arg
        op_index = arguments.index(arg)
        first_number = int(arguments[op_index - 1 ])
        second_number = int(arguments[op_index + 1])

if operation == "+":
    print (first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
else:
    print("Wrong operation")


