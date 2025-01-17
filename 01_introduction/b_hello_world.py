#!/usr/bin/python3
"""
Purpose: Basic PEP 8 guidelines
    shebang line

PEP - Python Enhancement Proposal
Pep 8 - coding style guide

This is docstring

"""

# print as a statement in python 2 & 3
print("hello world!")
print(True)
print("True", 123, None)

def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("uday")