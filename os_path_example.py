# Task: Path Operations
# Objective 6.1 - Perform basic file system operations using built-in modules
#
# Instructions:
# Use the os.path module to extract information from the file path below.
# 1. Get the filename from the path using os.path.basename
# 2. Get the directory from the path using os.path.dirname
# 3. Split the filename into name and extension using os.path.splitext
# 4. Build a new path by joining the directory with "notes.txt" using os.path.join
#
# Expected output:
# filename: essay.txt
# directory: /projects/homework
# name: essay
# extension: .txt
# new path: /projects/homework/notes.txt

# Your module import code here

import os

# path = "projects/homework/essay.txt"
#
# filename = os.path.basename(path)
# directory = os.path.dirname(path)
#
# print(filename)
# print(type(filename))
#
# name, extension = os.path.splitext(str(filename))
# print(name)
# print(extension)
# new_path = os.path.join(directory, "notes.txt")
#
# # ---------- DO NOT modify below this line ----------
# print("filename:", filename)
# print("directory:", directory)
# print("name:", name)
# print("extension:", extension)
# print("new path:", new_path)


import math

num_1 = -2

pow_num_1 = math.pow(num_1, 2)

print(pow_num_1)

sqrt_num_1 = math.sqrt(pow_num_1)

print(sqrt_num_1)