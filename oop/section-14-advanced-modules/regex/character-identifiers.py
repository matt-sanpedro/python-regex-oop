import re

text = 'My phone number is 777-555-1234'
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())

# using groups with the compile function
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())

# or operator for searching multiple terms
print(re.search(r'cat|dog', 'The cat is here'))
print(re.search(r'cat|dog', 'The dog is here'))

# wildcard operator, acts as a placement
print(re.findall(r'\w+at', 'The cat in the hat sat there.  Then went splat!'))

# start with: ^
print(re.findall(r'^\d', '1 is a number'))

# ends with: $
print(re.findall(r'\d$', 'The number is 7'))

# exclusion: [^]
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = 'This is a string!  But it has punctuation.  How can we remove it?'
clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))

# find the hyphen words: good practice to use brace notation to enable pattern combinations
text = 'Only find the hypen-words in this sentence.  But you do not know how long-ish they are.'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern, text))

# parenthesis for multiple matching
text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar?'

print(re.search(r'cat(fish|nap|erpillar)', textthree))