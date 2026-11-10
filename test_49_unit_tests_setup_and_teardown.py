# Exercise 49: Setup and Teardown
# Topic: unit_tests
#
# Task:
# Write tests that create a temporary directory and file, check existence and contents, then clean up.
#
# Requirements / hints:
# Use unittest setUp()/tearDown(), os, and tempfile.
#
# Write your solution below.

import unittest

class Test1(unittest.TestCase):

    def test_something(self):
        with open("test.txt", "w") as file:
            file.write("test")

        self.assertTrue("test.txt")