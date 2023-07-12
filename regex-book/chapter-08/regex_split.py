import re

'''
Split the given string to form a list
'''
my_str = input('Enter your string: ')
pattern1 = re.split(r"\s", my_str)      # split by space and output as list
pattern2 = re.split(r"s", my_str)       # split by chracter "s" and output as list
print('Using \s will output result: ', pattern1)
print('Using s will output result: ', pattern2)
