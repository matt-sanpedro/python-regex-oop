import re

'''
PROBLEM STATEMENT:
Write a program using RegEx that will replace all the digits in a string with an exclamation (!) sign
'''
pattern = re.compile(r"")
my_string = input('Enter a string: ')
pattern = re.compile(r"\d+")

# substitution
result = pattern.sub('_', my_string)
print(result)
