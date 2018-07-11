import pyperclip
import re

"""

Python3 script that takes a string from the clipboard
with the contents of brazilians phone numbers
and email addresses, filters them, prints them on the
terminal and copies to clipboard.

"""


def getPhoneNumber(string):
    phoneRegex = re.compile(r"""(
      (\+\d{2})?                  # country code
      (\s|\.)?                    # separator
      (\d{2})?                    # area code
      (\s|\.)?                    # separator
      ([9])?                      # 9 upfront, for cell numbers
      (\d{4})                       # first 4 digits
      (\s|-|\.)?                   # separator
      (\d{4})                       # last 4 digits
      )""", re.VERBOSE)
    match_list = phoneRegex.findall(string)
    return match_list


def getEmail(string):
    emailRegex = re.compile(r"""(
     [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
     [a-zA-Z0-9.-]+         # domain name
     (\.[a-zA-Z]{2,4})      # dot-something
     )""", re.VERBOSE)
    match_list = emailRegex.findall(string)
    return match_list


text = str(pyperclip.paste())
matches = []
phones = getPhoneNumber(text)
emails = getEmail(text)
for groups in phones:
    if groups[5] != "":
        phoneNum = " ".join(
            [groups[1], groups[3]]
        )

        phoneNum += "".join([" ", groups[5], groups[6], "-", groups[8]])
    else:
        phoneNum = " ".join([groups[1], groups[3]])
        phoneNum += "".join([" ", groups[6], "-", groups[8]])
    matches.append(phoneNum)

for groups in emails:
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
