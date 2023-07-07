import re

'''
FINAL TASK CRITERIA FOR PASSWORD VALIDATOR:
1. Must be at least 8 characters long
2. Must contain at least one:
    - number
    - special character
3. Must have first character in uppercase
'''

pattern = re.compile(r'')
password_length = 8

while True:
    my_str = input('Enter a password: ')

    # entering "done" will exit out of while loop
    if my_str == 'done': break
    
    # password length criteria
    if (8 > len(my_str)):
        print('Password must be of minimum 8 characters')

    if re.search(r'[!@#$%]', my_str) is None:
        print('Password must have 1 special character')
    
    if re.search(r'\d', my_str) is None:
        print('Password must have 1 digit')

    if my_str and not my_str[0].isupper():
        print('First character must be a capital letter')

    elif re.match(r'[A-Za-z0-9@#$%^&]{8,}', my_str):
        pattern = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        result = pattern.match(my_str)
        print(f'Valid password: {my_str}')
        break

    else:
        print('Password Invalid')