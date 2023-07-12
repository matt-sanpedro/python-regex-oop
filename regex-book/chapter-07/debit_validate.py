import re

'''
Debit Card Number:
- There are 16 digits in a debit or credit card number
- Arranged in 4 sets of 4 digits separated by space
'''
pattern = re.compile(r'')
num = input('Enter your Debit Card Number: ')

if len(num) == 19:
    result = re.match(r"[\d]{4}\s[\d]{4}\s[\d]{4}\s[\d]{4}", num)
    print('Debit Card Number entered is in correct format')
else:
    print('Please enter Debit Card Number in correct format')
    