# Exercise 28: Multiple Lines in Memory
# Topic: io
#
# Task:
# Store five lines in StringIO and read them one at a time.
#
# Requirements / hints:
# Use readline(); avoid extra blank lines.
#
# Write your solution below.

import io

store = io.StringIO()

store.write("John Doe")
store.write("Jane Doe")
store.write("John Cena")
store.write("Rick Ashley")
store.write("Bob")

for line in store.readlines():
    print(line)