# Exercise 22: Argument Counter
# Topic: sys
#
# Task:
# Count command-line arguments excluding the script name.
#
# Requirements / hints:
# Example: python args.py one two three -> Number of arguments: 3.
#
# Write your solution below.

import sys

args = sys.argv
args_2 = ['22_sys_argument_counter.py', '-l', 'John', '-p', 'Passwrod']

print(args)
print(type(args))

arg_len = len(args) - 1
print(f" Number of arguments: {arg_len}")