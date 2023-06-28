# enters if block and executes
if 'dog' in 'my dog is great':
    print('yes')

text = "The agent's phone number is 858-656-0089.  Call soon!"
print('phone' in text) # True

# import the re module to perform regex operations
import re

pattern = 'NOT IN TEXT'
print(re.search(pattern, text)) # None

pattern = 'phone'
print(re.search(pattern, text)) # <re.Match object; span=(12, 17), match='phone'>

# creating the match object
match = re.search(pattern, text)
print(match.span(), match.start(), match.end())

# if more than one match occurs, only returns first match on span method
text = 'my phone once, my phone twice'
match = re.search(pattern, text)
print(match.span(), match.start(), match.end())

# using the findall method
matches = re.findall(pattern, text)
print(matches) # returns a list of string of the matches

# using the finditer method
for match in re.finditer('phone', text):
    # returns the matched text
    print(match.group())
