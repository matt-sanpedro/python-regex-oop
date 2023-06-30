import re

my_str = 'Bond! James Bond'
pattern = re.findall(r"^B", my_str)

if pattern:
    print("Yes, the string starts with 'B'")
else:
    print('No match')

# verify first letter without the ^ operator
my_str = 'Patience is the key to success'
result = re.findall("\APatience", my_str)
print(result)

if result:
    print('Yes, there is a match!')
else:
    print('No match')
