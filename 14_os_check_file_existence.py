# Exercise 14: Check File Existence
# Topic: os
#
# Task:
# Ask for a path and report whether it exists.
#
# Requirements / hints:
# Use os.path.exists().
#
# Write your solution below.

import os

if os.path.exists("hello.txt"):
    print('File exists')
else:
    print('File does not exist')