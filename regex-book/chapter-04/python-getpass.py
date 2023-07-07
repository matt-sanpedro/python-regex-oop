import re
import getpass

'''
Motivation:
I want to type a potentially new password in form of dots in case of peering eyes

- getpass().getpass() prompts the user for password without echoing 
- improves the security of password while typing
'''

pattern = re.compile(r'')

while True:
    my_str = getpass.getpass('Enter a password: ')
    print(f'Oh great, you entered: {my_str}')

    if my_str == 'done': break