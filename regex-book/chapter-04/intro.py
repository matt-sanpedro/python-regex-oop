import re

'''
Chapter 4
Focuses on Validation with Regex, ie. password validation

Task 1:
Write a program to simply generate a password that consists of numbers and characters

Implementation:
1. Enter a string
2. Use \d to validate digits
3. Use \D for non-digits
4. Steps 2 and 3 can be alpha-numeric
5. Print result with message
'''
pattern = re.compile(r'')
# password = 'mark11'
password = input('Enter a password: ')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'[A-Za-z0-9@#$%^&]')
pattern = re.compile(r'[!@#$%^&*,/\?<>~]')
result = pattern.match(password)
if result:
    print(f'Valid password: {password}')
else:
    print('Password invalid')
