import re

'''
Aadhar Card Number Validation

Implementation:
1. Enter Aadhar card number
2. This 12 digit number is written as 3 sets of 4 digits separated by a "-" or "/" or space
3. The length of the numbers should be 12
4. \d will match digits in card number, \d{4} represents matching digits four times
5. Print validation success or error message

Notes:
(-| |/) -> dash or space or slash, regex executes this group and declare valid character in "group 1"
(\1)    -> refers back to group 1 or more specifically, the character that was found in group 1 position
'''
pattern = re.compile(r'')
num = input('Enter the 12 digit Aadhar Number: ')

if len(num) == 14:
    result = re.match(r"\d{4}(-| |/)\d{4}(\1)[\d]{4}", num)
    print('Aadhar number is in correct format')
else:
    print('Please enter the Aadhar number in correct format')
    