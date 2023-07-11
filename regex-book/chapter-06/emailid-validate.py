import re

'''
String Validation III (Email ID)
- Usually when creating an account, an email is sent with a verifying link
- Therefore, the created email ID must be validated with regex

Implementation:
1. Can begin with any character (abc, 123abc, #abc, etc.)
2. Can have two or more parts (abc_def, abc.def, etc.)
3. Steps 1 and 2 is part I of email ID
4. After part I, for part II there must be a "@" symbol
5. Finally, after mail server name, "." sign followed by com or edu or org, etc.
6. Sometimes, the last part goes like: .co.uk or .gov.in (there are two dots in this edge case)

Notes:
- Part I can have many solution possibilities
'''
pattern = re.compile(r'')
user_login = input('Enter the email ID: ')
'''
- starts with an "@" sign
'''
# pattern = re.match(r'^@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*(\.[a-zA-Z]{1,255})', user_login)
# pattern = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)'\
#                    '*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)'\
#                    '*(\.[a-zA-Z]{1,255})$',  
#                    user_login)

# \W allows special character at beginning
# | the pipe symbol is an "or" operator so email can begin with special character or any alphanumeric
pattern = re.match(r'^(\W|[_a-z0-9-]+)*(\W[_a-z0-9-]+)'\
                   '*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)'\
                   '*(\.[a-zA-Z]{1,255})$',  
                   user_login)


# line breaks in python with backslash (\)
my_string = 'Simplifying Regular Expression '\
            'Using Python is great for automation '\
            'and learning regular expression.'
# print(my_string)

if pattern == None:
    print('Invalid Email ID')
else:
    print(pattern)