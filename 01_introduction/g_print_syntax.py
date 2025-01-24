"""
Purpose: print() function syntax and usage
    Escape Sequences
        - character whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character

        r'' - raw string

"""

print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")

print()

# To ignore the escape sequences
print("hello \tworld \\npython")
print(r"hello \tworld \npython")
print()

print("C:\my\newfolder") # noqa: w605
print(r"C:\my\newfolder")
print()

# print(data, sep = ' '), end = '\n'

print("hello")  # defaukt end='\n'
print("world")

print("hello", end = '\n')
print("world", end = '\n')

print("hello", end = '\t')
print("world", end = '\n')

print("hello", end = '___')
print("world", end = '\n')

print("hello", "python", 1232, end = '\t')
print("world")

print("hello", "python", 1232, end = '\t', sep = ";")
print("world")