#!/bin/python3
import re

"""

Simple Python3 script that reads a string and returns a Match Object
with the contents of the brazilians phone numbers that it found

"""


def getPhoneNumber(string):
    phoneNum = re.compile(r"(\+\d{2} )?(\d{2} )?(\d{4}-\d{4})")
    mo = phoneNum.findall(string)
    return mo


string = input("Type Line:\n")
numbers = getPhoneNumber(string)

print(numbers)
