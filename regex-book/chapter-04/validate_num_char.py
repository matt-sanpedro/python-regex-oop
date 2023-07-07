import re

'''
Task 3:
Write a program to validate a password that consists of numbers and characters
but there should be NO special character present at any position

Implementation:
'.*\W+' -> pattern to look across entire string for non-alphanumeric characters
'''

while True:
    userpassword = input('Enter a password: ')
    if userpassword == 'done': break
    # check for any non-alphanumeric character match
    result = re.match(r'.*\W+', userpassword)
    
    if result:
        print('Invalid.  Some special character is present')
    else:
        result = re.match(r'\w+', userpassword)
        print(f'{result.group()} is a valid password')
        