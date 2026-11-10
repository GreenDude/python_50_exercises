# Exercise 13: Create a Directory
# Topic: os
#
# Task:
# Create a directory named python_practice without crashing if it already exists.
#
# Requirements / hints:
# Use os.makedirs().
#
# Write your solution below.
import os

dir_path = "python_practice"
if os.path.exists(dir_path):
    os.mkdir(dir_path)
