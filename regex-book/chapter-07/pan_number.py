import re

'''
PAN Card (Personal Account Number Card)
Can also be thought of as social security card, required for filing taxes, open bank account

Implementation:
1. PAN is a 10 digit number (without space) and includes alphanumeric characters
2. The PAN regex pattern is 5 characters followed by 4 digits and 1 chracter at last
3. The regex pattern is: \D{5}-\d{4}-\D{1}
4. Starts and ends with a non-digit character, anchors ^ and $ will be useful

Notes:
- \D used for non-digits
'''
pattern = re.compile(r'')
num = input('Enter your PAN card: ')

if re.match(r'.*[a-z]', num):
    print('Please enter PAN card with NO lowercase characters')
elif len(num) == 10:
    # result = re.match(r"^[\D]{5}[\d]{4}[\D]{1}$", num)
    result = re.match(r"^[A-Z]{5}[\d]{4}[A-Z]{1}$", num)
    print('PAN card number entered is in correct format')
else:
    print('Please enter PAN card number in correct format')
