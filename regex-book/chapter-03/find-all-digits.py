import re

my_string = input('Enter a string: ')

# find all digits and return result as list
result = re.findall(r"\d", my_string)
print(result)
