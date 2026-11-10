# Exercise 10: Student Grades
# Topic: files
#
# Task:
# Prompt for student names and grades, append multiple records to grades.txt, then display saved records.
#
# Requirements / hints:
# Example lines: Alice,90 and Bob,85.
#
# Write your solution below.

with open("grades.txt", "r+") as f:
    student_1 = "Alice"
    student_2 = "Bob"
    grades_1 = "22"
    grades_2 = "33"

    f.write(student_1 + "," + grades_1 + "\n")
    f.write(student_2 + "," + grades_2 + "\n")