import re

'''
the search function 
- searches the string for a match, and returns a Match object if there is a match
- if there is more than one match, only first occurrence is returned
'''
def check_result(result):
    print(result)
    if result:
        print('Yes, there is a match!')
    else:
        print('No match')

# using the search function with two possible matches
my_str = 'The truth is...I am The Iron Man'
result = re.search("The", my_str)
check_result(result)

# using the findall function with two possible matches returns a list with no span
result = re.findall("The", my_str)
check_result(result)
