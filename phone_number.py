#!/bin/python3
import re

"""

Simple Python3 script that return a Match Object
with the contents of a brazilian phone number

"""


def getPhoneNumber(string):
    phoneNum = re.compile(r"(\+\d{2} )?(\d{2} )?(\d{4}-\d{4})")
    mo = phoneNum.search(string)
    return mo


string = input("Type Line:\n")
number = getPhoneNumber(string)

print("country code: {}".format(number.group(1)))
print("area code: {}".format(number.group(2)))
print("phone number: {}".format(number.group(3)))
