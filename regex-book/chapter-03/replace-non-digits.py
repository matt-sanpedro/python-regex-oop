'''
Write a program that will replace all the non-digits in a string with an underscore (_)

1. Input a string.  The string should have non-digits also
2. Find out non-digits and replace with underscore
3. Print new string with an underscore
'''
import re
# line below not compulsory to write, but good practice
pattern = re.compile(r"")
my_string = input("Enter a string: ")

# check for any non-digits one or more
# pattern = re.compile(r"\D+")
# can also use negation one or more
pattern = re.compile(r"[^0-9]+")

# check for any non-digits one by one
# pattern = re.compile(r"\D")
# can also use negation
pattern = re.compile(r"[^0-9]")


# perform the substitution below
result = pattern.sub("_", my_string)
print(result)
