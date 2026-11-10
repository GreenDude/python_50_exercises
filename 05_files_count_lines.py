# Exercise 05: Count Lines
# Topic: files
#
# Task:
# Count the number of lines in students.txt.
#
# Requirements / hints:
# Expected output for five lines: Total lines: 5.
#
# Write your solution below.

string_count = 0
with open("students.txt", "r") as f:
    print (f.readlines())
    f.seek(0)
    for line in f.readlines():
        string_count += 1

    num = len(f.readlines())

print  (string_count)
print (num)