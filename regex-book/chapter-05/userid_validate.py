import re

'''
String Validations II (User ID Validation)

Implementation:

Regex positive and negative look ahead to avoid successive use of ".." or "__"
a [? ! b] -> a not followed by b
[._] [? ! ._] -> dot underscore not followed by dot underscore
'''
pattern = re.compile(r"")

while True:
    username = input('Enter a username: ')
    # matches most string inputs
    # pattern = re.compile(r"^[a-zA-Z0-9._]|[a-zA-Z0-9]$")
    # NO string seems to match pattern below
    # pattern = re.compile(r"^[a-zA-Z0-9_]([._](?![._])|[a-zA-Z0-9])$")

    # using the \w with quantifier to get restricted amount of characters
    # does NOT work with "tony__stark"
    pattern = re.compile(r"^[\w]([._](?![._])|[\w]){7,20}[\w]$")
    result = pattern.match(username)
    print(result)

    if result:
        print(f"Username formation success: {username}")
        break
    else:
        print("Invalid Username, please try again")
