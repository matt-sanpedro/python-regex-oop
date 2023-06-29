# Table 1: Special Sequences
| Character    | Description
| :-------- | ------- 
| .  | Matches any single character except newline
| \d | This matches any digit [0-9]
| \D | This matches non-digit characters [^0-9]
| \s | This matches whitespace character [\t\n\r\f\v]
| \S | This matches non-whitespace character [^ \t\n\r\f\v]
| \w | This matches alphanumeric character [a-zA-Z0-9_]
| \W | This matches any non-alphanumeric character [^a-zA-Z0-9_]
| \A | Returns a match if the specified characters are at the beginning of the string
| \b | Returns a match where the specified characters are at the beginning or the end of a word
| \B | Returns a match where the specified characters are present, but NOT at the beginning (or the end) of a word
| \Z | Returns a match if the specified characters are at the end of the string


# Table 2: Quantifiers
(Specify number of characters to match)

| Character    | Description | Example | Sample Match
| :-------- | ------- | ------- | ------- 
| + | One or more | \w+ | ABCDEF097
| {2} | Exactly 2 times | \d{2} | 01
| {1,} | One or more times | \w{1,} | smiling
| {2,4} | 2, 3, or 4 times | \w{2,4} | 1234 
| * | 0 or more times | A*B | AAAAB
| ? | Once or none | \d+? | 1 in 12345


# Table 3: Sets
(Set of characters inside a pair of square brackets [] with a special meaning)

| Character    | Description
| :-------- | ------- 
| [arn] | Returns a match where one of the specified characters (a, r, or n) are present
| [a-n] | Returns a match for any lower case character, alphabetically between a and n
| [^arn] | Returns a match for any character EXCEPT a, r, and n
| [0123] | Returns a match where any of the specified digits (0, 1, 2, or 3) are present
| [0-9] | Returns a match for any digit between 0 and 9
| [0-5][0-9] | Returns a match for any two-digit numbers from 00 and 59
| [a-zA-Z] | Returns a match for any character alphabetically between a and z, lower OR upper case
| [+] | In sets, +, *, .,  &#124;, (), $, {} has no special meaning, so [+] means: return a match for any + character in the string
