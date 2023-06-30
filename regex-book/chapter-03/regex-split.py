import re

# the split function returns a list where the string has been split at each match
my_str = 'My name is Cable'
result = re.split("\s", my_str)
print(result)

# split only two words and not the remaining
result = re.split("\s", my_str, 2)
print(result)
