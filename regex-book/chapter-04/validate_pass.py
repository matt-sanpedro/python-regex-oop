import re
pattern = re.compile(r'')

'''
Task 2:
Write a program to simply generate a password that consists of numbers and characters 
and it should be at least 6 characters long
'''

while True:
    my_str = input('Enter a password: ')
    if (6 > len(my_str)):
        print('Password must be of minimum 6 characters')
    elif re.match(r'[A-Za-z0-9@#$%^&]{1,6}', my_str):
        # {1,6} -> pattern caution: any character written after 6th position will be excluded
        # caution on character matching below:
        # still can add "." after alphanumeric character anmmd password will be valid
        pattern = re.compile(r'[A-Za-z0-9@#$%^&+=]{1,6}')
        result = pattern.match(my_str)
        print(f'Valid password: {result}')
        break
    else:
        print('Password Invalid')
