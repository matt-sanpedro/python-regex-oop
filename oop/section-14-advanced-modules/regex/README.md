# Regular Expressions (Regex) for Python

## Introduction
Capability includes searching for general patterns in text data

For an email with format:
    - user@email.com

The following pattern is searched: 
    - 'text' + '@' + 'text' + '.com'

## Phone Number Example
- Phone number: (555)-555-5555
- Regex pattern option 1: r"(\d\d\d)-\d\d\d-\d\d\d\d"
- Regex pattern option 2: r"(\d{3})-\d{3}-\d{4}"

The "identifier" \d stands for digit

# Character Identifiers
| Character    | Description | Example Pattern Code | Example Match
| :-------- | ------- | ------- | ------- |
| \d  | A digit    | file_\d\d | file_25
| \w | Alphanumeric | \w-\w\w\w | A-b_1
| \s  | White space | a\sb\sc | a b c
| \D | A non digit | \D\D\D | ABC
| \W | Non-alphanumeric | \W\W\W\W\W | *-+=)
| \S | Non-whitespace | \S\S\S\S | Yoyo

# Character Quantifiers
| Character    | Description | Example Pattern Code | Example Match
| :-------- | ------- | ------- | ------- |
| +  | Occurs one or more times | Version \w-\w+ | Version A-b1_1
| {3} | Occurs exactly 3 times | \D{3} | abc
| {2,4} | Occurs 2 to 4 times | \d{2,4} | 123
| {3,} | Occurs 3 or more | \w{3,} | anycharacters
| * | Occurs zero or more times | A* B* C* | AAACC
| ? | Once or none | plurals? | plural