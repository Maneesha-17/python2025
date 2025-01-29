"""
Purpose: Multiple statements in same libe
    , logic separator
    ; statement completion operator
"""

print("hello" "world")
print("hello", "world")

print("Hello", 21312)
# print("Hello" 21312) # SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("Hello", 21413, 212,  124 + 45 - 3)
print()

# Method 1 
num1 = 100
num2 = 200
sum_of_numbers = num1 + num2
print("Sum of Numbers:", sum_of_numbers)

# Method 2 
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2
print("Sum of Numbers:", sum_of_numbers)

# python -c "print('Hello world')"