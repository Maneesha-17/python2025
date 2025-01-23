"""
Purpose: Importance of Indentation
"""

print("Hello world 1")
#  print("Hello world 2") #IndentationError: unexpected indent
print("Hello world 3")

# block code - if, else, for, while, def, class
# if 12>3:
# print('12 is greater than 3') 
# IndentationError: expected an indented block after 'if' statement on line 10

if 12 > 3:
    print('12 is greater than 3')

if 12 > 3:
    print('12 is greater than 3')
else:
    print('12 is lesser than 3')