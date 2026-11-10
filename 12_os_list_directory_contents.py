# Exercise 12: List Directory Contents
# Topic: os
#
# Task:
# Print the files and folders in the current directory.
#
# Requirements / hints:
# Use os.listdir().
#
# Write your solution below.

import os

current_dir = os.getcwd()

print(current_dir)

for name in os.listdir():
    print (name)