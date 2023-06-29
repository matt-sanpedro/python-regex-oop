# Simplifying Regular Expressions Using Python
- Authors: Abhishek Singh, Zohaib Hasan

## Introduction
- Python has a built-in package called *re* for regular expressions
- 1st line of code to import module
```
import re
```
- 2nd line of code will compile a RegEx pattern for subsequent matching
    * Handy to compile RegEx when it will be used several times in your program
```
pattern = re.compile(r"")
```
- The prefix, ```r""```, indicates whatever is in the double quotes should be treated literal and not escape characters for Python