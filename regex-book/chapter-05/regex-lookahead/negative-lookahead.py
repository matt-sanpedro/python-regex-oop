import re

'''
NEGATIVE LOOK AHEAD
Opposite of look ahead to assure that the search string is not followed by <lookahead_regex>

Example syntax:
(?!<lookahead_regex>)
'''
def show_example(example):
    if example:
        print('Pattern:', example.group())
        print('Pattern found from index:', example.start(), 'to', example.end())
    else:
        print('Pattern not found')
    print('\n')

# search string
searchterm = 'geeksforgeeks'
# searchterm = 'geeks123'

# positive lookahead
example1 = re.search('geeks(?=[a-z])', searchterm)

# negative lookahead
example2 = re.search('geeks(?![a-z])', searchterm)

# output results
show_example(example1)
show_example(example2)
