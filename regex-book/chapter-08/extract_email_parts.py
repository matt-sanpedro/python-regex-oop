import re

'''
Given email ID, determine username and password
- group()           -> function allows extracting specific parts of matching text by what is inside parenthesis
- pattern.group()   -> returns whole match
- pattern.group(1)  -> returns the first part
'''
my_str = input('Enter the string: ')
match = re.search(r"([\w.-]+)@([\w.-]+)", my_str)

if match:
    print('The email ID present in the input string is:', match.group())
    print('The username is:', match.group(1))
    print('The hostname is:', match.group(2))
else:
    print('No or invalid email ID is present')
    