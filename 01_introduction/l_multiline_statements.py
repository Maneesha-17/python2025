"""
Purpose: Multi Line statements

"""

sum_of_values = 123 + 23 - 123 * 2 / 12
print(sum_of_values)

sum_of_values = 123 + 23 - 123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / 22 * 45
print(sum_of_values)

"""
PEP 8: 

1) lines should be 79 characters in length or less
2) conntinuations of long expressions onto additional lines\
   
"""

sum_of_values = 123 + 23 - 123 * 2 / 12 - 45 + \
98 / 23 * 4 + 98 - 12 / 22 * 45 + 123 + 23 - \
123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / \
22 * 45 * 123 + 23 - 123 * 2 / 12 - 45 + \
98 / 23 * 4 + 98 - 12 / 22 * 45 
print(sum_of_values)

# '\' is called line continuation operator
# '#' can not be used after line continuation operator

# braces alongside line continuation operator
sum_of_values = (123 + 23 - 123 * 2 / 12 - 45 + \
98 / 23 * 4 + 98 - 12 / 22 * 45 + 123 + 23 - \
123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / \
22 * 45 * 123 + 23 - 123 * 2 / 12 - 45 + \
98 / 23 * 4 + 98 - 12 / 22 * 45 )
print(sum_of_values)

# braces alone
sum_of_values = (123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 + 123 + 23 - 
123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / 
22 * 45 * 123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 )
print(sum_of_values)

sum_of_values = [123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 + 123 + 23 - 
123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / 
22 * 45 * 123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 ]
print(sum_of_values)

sum_of_values = {123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 + 123 + 23 - 
123 * 2 / 12 - 45 + 98 / 23 * 4 + 98 - 12 / 
22 * 45 * 123 + 23 - 123 * 2 / 12 - 45 + 
98 / 23 * 4 + 98 - 12 / 22 * 45 }
print(sum_of_values)