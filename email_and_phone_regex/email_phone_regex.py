import pyperclip
import re


def getPhoneNumber(string):
    phoneRegex = re.compile(r"""(
    (\+\d{2})?                  # country code
    (\s|\.)?                    # separator
    (\d{2})?                    # area code
    (\s|\.)?                    # separator
    \d{4}                       # first 4 digits
    (\s|-|\.)?                   # separator
    \d{4}                       # last 4 digits
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
    matches.append(groups[0])
for groups in emails:
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
