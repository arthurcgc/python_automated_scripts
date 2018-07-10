#!/bin/python3
import re

"""

Simple Python3 script that reads a string and returns a Match Object
with the contents of the brazilians phone numbers that it found

"""


def getPhoneNumber(string):
    phoneRegex = re.compile(r"""(
    (\+\d{2})?                  # country code
    (\s|\.)?                    # separator
    (\d{2})?                    # area code
    (\s|\.)?                    # separator
    \d{4}                       # first 4 digits
    (\s|-|\.)                   # separator
    \d{4}                       # last 4 digits
    )""", re.VERBOSE)
    match_list = phoneRegex.findall(string)
    return match_list


string = input("Type Line:\n")
numbers = getPhoneNumber(string)

print(numbers)
