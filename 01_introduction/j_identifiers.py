"""
Purpose : Identifiers in Python

    Variable
        1. Keyword --> words which have some meaning
        2. Identifer -> words which are defined 

"""

# loading module
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert',
#   'async', 'await', 'break', 'class', 'continue',
#     'def', 'del', 'elif', 'else', 'except', 
#     'finally', 'for', 'from', 'global', 'if', 
#     'import', 'in', 'is', 'lambda', 'nonlocal', 
#     'not', 'or', 'pass', 'raise', 'return', 'try',
#       'while', 'with', 'yield']
print()

print(True)
# print(true)

my_value = "something"
print(my_value)

# True = "something" SyntaxError: cannot assign to True

print(keyword.iskeyword("True"))     # True
print(keyword.iskeyword("true"))     # False
print(keyword.iskeyword("my_value")) # False

# Identifiers - User-defined variables
#   - Naming Convention
#     1. Keywords should not be used as identifiers
#     2. first character: a-z, A-Z, _
#     3. remaining chars: a-z, A-Z, _, 0-9

# ---- Rule 1
# True = 123        # Syntax error
# None = 'Nothing   # Syntax error

# PEP 8 - Don't create identifiers which are similar to keywords
true = 123
none = "something"

true_value = 123
none_result = "nothing"

# ---- Rule 2 & 3
name = "priya"
name_of_student = "priya"
first_name = "priya"
student_1 = "priya"
class_02_a = "python comment operations"
first____child = "satvik"

# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12

# $name = "Priyanka"
# name-of-student = "Priyanka"
# name of student = "Priyanka"
# 1st_name = "Priyanka"

_2nd_student = 'someone'

_job = "software development"
__role = "Production support"
____salary = 121312144

# OOP -> name mangling
# variable -> Public variable
# _variable -> Protected variable
# __variable -> Private variable

# __variable__ -> Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print("__name__ =", __name__) # __main__
print("__file__ =", __file__) # /workspaces/python2025/01_introduction/j_identifiers.py

# print("__jay__=", __jay__)