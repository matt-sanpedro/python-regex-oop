import re

'''
DOB Validation proposed format: 
dd-mm-yyyy or in regex \d{2}-\d{2}-\d{4}
Length has to be 10 including spaces
'''
pattern = re.compile(r'')
num = input('Enter the Date of Birth in dd-mm-yyyy format: ')

if len(num) == 10:
    result = re.match(r"[\d]{2}-[\d]{2}-[\d]{4}", num)
    print('Date of Birth is in correct format')
else:
    print('Please enter Date of Birth in correct format')
