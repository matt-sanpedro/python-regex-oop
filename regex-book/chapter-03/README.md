# String Manipulation using RegEx
Goal: replace or substitute non-digits with an underscore sign

# On Boundaries: ^ and $
- ^ marks start, also known as Hat
- $ marks end of regular expression
- When used in square brackets, the ^ is denoted negation

# Match Object
- Contains information about the search and result
- Some attributes related to search operation include:
    * .span() -> returns tuple containing the start-, and end positions of the match
    * .string -> returns the string passed into the function
    * .group() -> returns part of the string where there was a match