import re

'''
LOOK AHEAD
- An assertion in Python regular expressions to determine success or failure, 
whether pattern is ahead.  
- Also called zero-width assertions since they don't match anything

Example of positive lookahead
(?=<lookahead_regex>)

(?=[a-z])
Specifies what follows geeks must be a lowercase alphabetic character
'''
def show_example(example):
    if example:
        print('Pattern:', example.group())
        print('Pattern found from index:', example.start(), 'to', example.end())
    else:
        print('Pattern not found')
    print('\n')

example = re.search(r'geeks(?=[a-z])', "geeksforgeeks")
# example = re.search(r'geeks(?=[a-z])', "geeks123")
# example = re.search(r'[._](?![._])', "geeks_forgeeks")

# without look ahead
example2 = re.search(r'geeks([a-z])', 'geeksforgeeks')

show_example(example)
show_example(example2)
