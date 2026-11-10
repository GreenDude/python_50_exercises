# Exercise 18: Environment Variables
# Topic: os
#
# Task:
# Print PATH; read MY_APP_MODE, defaulting to "development" when missing.
#
# Requirements / hints:
# Use os.environ and os.getenv().
#
# Write your solution below.

import os

environ_dict = os.environ
path_value = environ_dict.get("PATH")
print (path_value)

my_app_mode = os.getenv("MY_APP_MODE")
if my_app_mode is None:
    my_app_mode = "development"
print(my_app_mode)