#!/usr/bin/python3
"""
Purpose: Working with comment operator
    - Once # is encounteres, complete line from that position is ignored
    - PEP 8 recommends one white space after # operator
    - Comments
        - Single Line comment #
        - Multi-line comment - Python doesn't support


Question: Why python doesn't have multi-line comment operator
Answer: Python is a interpreter based language, means each line executes

Python code ---> line by line -> assembly -> Machine

ctrl + / - multi-line comment/uncomment

print("hello world1")
"""

print("Hello world2")
# print("Hello world3")

print("Hello #world4")
print("hello", "world5", sep="#")
# print("hello", "world5")

print("hello world6") # 1234jk12390ruiufijfvui7598429$%&^*&
print("hello world7") # this is about the world

print("hello world8") #
# print('hello world8'#) SyntaxError: '(' was never closed
