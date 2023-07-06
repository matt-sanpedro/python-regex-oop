import re

'''
IMPLEMENTATION
Write a program to search for an upper case character at the beginning of a word,
and print its position

\b -> returns a match where the specified characters are at the beginning or end of the word
\w -> returns a match where the string contains any word chracters
'''
my_str = 'I am Iron Man'
result = re.search(r"\bM\w+", my_str)
if result:
    print(result.span())
else:
    print('No match')

'''
IMPLEMENTATION
Write a program to search for an upper case character at the beginning of a word,
and print that complete word
'''
print(result.group())

'''
IMPLEMENTATION
Write a program to search for the character at the beginning of a word,
and print that complete word
'''
my_input = 'Avengers'
dotsequence = re.search(r'\b[a-zA-Z]vengers', my_input)
# dotsequence = re.search(r'^[a-zA-Z]vengers', my_input)
print(dotsequence)
print(dotsequence.string)
