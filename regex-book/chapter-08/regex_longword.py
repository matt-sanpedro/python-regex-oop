import re

'''
Longest word in a string with regex matching

Implementation:
1. Check for words character by character, ie. non-whitespace character with \S+
2. Check for length of word
3. Define a variable which stores the maximum length of the word
4. If length of the word is equal to the maximum length of the word, 
   then maximum word length is present in input string
'''
my_str = input('Enter the string: ')
my_str = re.findall(r'\S+', my_str)
max_len = max(len(word) for word in my_str)
print('The maximum length of word in sentence is:', max_len)

for word in my_str:
    if len(word) == max_len:
        print('The longest word in sentence is:', word)
