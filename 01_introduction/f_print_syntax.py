"""
Purpose: Print() function syntax and usage
"""

name = "Almighty"  #str

print("name =", name)
print("Name of the student is name")

print("Name of the student is" + name)
print("Name of the student is " + name)
print()

print("Name of the student is", name)
print("Name of the student is", name, sep = " ")
print("Name of the student is", name, sep = "-")
print("Name of the student is", name, sep = "")
print()

print(1, 2, 3, 4, 5, 6) #default sep=' '
print(1, 2, 3, 4, 5, 6, sep = " ")
print()

print(1, 2, 3, 4, 5, 6, sep = "~")
print(1, 2, 3, 4, 5, 6, sep = "_")
print(1, 2, 3, 4, 5, 6, sep = ":")
print()

# NOTE: Python is a dynamic typed language
name = 1232
print("Name of student is", name)
# print("Name of student is" + name) #TypeError: can only concatenate str (not "int") to str

# NOTE: Python is a strictly typed language
print("1 + 2           =", 1 + 2) #addition
print("'1' + '2'       =", "1" + "2") # string concatenation
print()

# 1 + '2' #

print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + '2')
print()

print("int('234') =", int("234"))

# print("int('23.4') =", int('23.4')) # ValueError: invalid literal for int() with base 10: '23.4'
# print("int('two') =", int('two')) # ValueError: invalid literal for int() with base 10: '23.4'

print("Name of the student is" + str(name))
print("Name of the student is" + " " + str(name))