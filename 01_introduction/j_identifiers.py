"""

purpose: identifiers in python

    variables
        1. keyword -----> words which have some maning
        2. identifiers---> words which are defined by the user

        
"""

# loading a module

# import_keyword

#print(keyword.kwlist)
# ['false', 'None', 'True']
#print()


#print(true)

import keyword


my_value = "something"
print(my_value)  # identifier


#true = "something"
# syntax error: cannot assign to true


print(keyword.iskeyword("true"))  #true
print(keyword.iskeyword("true"))  #false
print(keyword.iskeyword("my_value"))  #  false


# --------------------------------------
# identiifrrs - users - defined variables
#  - naming convention
#       1. keywords should not be defined as identifiers
#       2. first character: a-z, A-Z, -
#       3.remaining characters: a-z, A-Z, -, 0-9

#  ---- rule 1
#   true = 123    # syntax error: cannot assign to true
#  None = 'Nothing'  # syntaxerror: cannot assign to False

# PEP 8 - dont create identifiers which are similar to eacch other
true = 123
none = "nothing"
