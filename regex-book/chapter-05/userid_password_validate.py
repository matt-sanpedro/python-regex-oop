import re

'''
UserID and Password Validation
Prohibits user from entering same value for userid and password
'''

pattern1 = re.compile(r"^[\w]([._](?![._])|[\w]){7,20}[\w]$")
pattern2 = re.compile(r"[A-Za-z0-9@#$%^&+=]{1,6}")

username = ''
password = ''

# while not pattern1.match(username) and not re.match(r'.*__', username):
while not pattern1.match(username) or re.match(r'.*__', username):
    username = input('Enter a username: ')

while not pattern2.match(password):
    password = input('Enter a password: ')

    # check if userid and password are the same
    if username == password:
        print('Username and Password cannot be the same')
        password = ''

print('Username and Password created successfully')
