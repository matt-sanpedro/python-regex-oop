import re

'''
IP Address Validation
- Each number in the set can range from 0 to 255
- Full IP addressing range goes from 0.0.0.0 to 255.255.255.255
'''
pattern = re.compile(r'')
num = input('Enter the IP address: ')
result = re.match('^[\d]{1,3}(\.)[\d]{1,3}(\.)[\d]{1,3}(\.)[\d]{1,3}$', num)

if result:
    print('IP Address entered is in correct format')
else:
    print('Please enter IP Address in correct format')
