# Exercise 41: Random Password Generator
# Topic: random
#
# Task:
# Ask for a password length; generate a password using digits.
#
# Requirements / hints:
# Use random.choice() and string. For real passwords, use secrets instead.
#
# Write your solution below.

import random

password_length = int(input("Please enter a password length: "))
password = ""

num_string = "0123456789"

# print (random.choice(num_string))

for i in range(password_length):
    password += random.choice(num_string)

print (password)

