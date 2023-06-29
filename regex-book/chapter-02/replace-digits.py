'''
Write a program that will replace all the digits in a string with an underscore (_)

1. Input a string.  The string should have digits also
2. Find out digits and replace with underscore
3. Print new string with an underscore
'''
import re
# line below not compulsory to write, but good practice
pattern = re.compile(r"")
my_string = input("Enter a string: ")

# check for any digits one or more
# pattern = re.compile(r"[0-9]+")
pattern = re.compile(r"\d+")

# check for any digits one by one
# pattern = re.compile(r"[0-9]")

# perform the substitution below
result = pattern.sub("$", my_string)
print(result)
