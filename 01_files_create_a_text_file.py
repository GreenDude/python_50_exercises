# Exercise 01: Create a Text File
# Topic: files
#
# Task:
# Create hello.txt and write "Hello, Python!" into it.
#
# Requirements / hints:
# Use open() with mode "w".
#
# Write your solution below.

with open("hello.txt", "w") as hello_file:
    hello_file.write("hello world")


try:
    with open("hello.txt", "r") as hello_file:
        hello_file.write("hello world")

except Exception as e:
    print(e)