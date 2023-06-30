import re

# write a program to verify the last letter of the input string is correct as it was entered

my_str = 'Bond!  James Bond 007'
pattern = re.findall("007$", my_str)

if pattern:
    print("Yes, the string ends with '007'")
else:
    print('No match')
