# Exercise 34: Rounding Numbers
# Topic: math
#
# Task:
# For [3.2, 4.7, -2.3, -5.8], print floor, ceil, and trunc for each.
#
# Requirements / hints:
# Explain differences for negative numbers.
#
# Write your solution below.

import math

number_list = [3.2, 4.7, -2.3, -5.8]

for i in number_list:
    print(math.floor(i))
    print(math.ceil(i))
    print(math.trunc(i))
    print("<><><><><><><><><><><><><><><><><><>")