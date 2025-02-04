"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithm:
----------
Step 1: Take a string in run-time and store in a variable
Step 2: Create a reverse string, from the given string, using string reversal
Step 3: Compare both with a condition and decide

"""

# test_string =  input("Enter any string : ")
# print("test_string =", test_string)

# reverse_string = test_string[::-1]
# print("Reverse string =", reverse_string)

# print(test_string == reverse_string)

# if test_string == reverse_string:
#     print(test_string, "is palindrome")
# else:
#     print(test_string, "is not a palindrome")


# assignment

sentence = input("Enter a sentence: ")
print("sentence =", sentence)


white_space_removed = sentence.replace(" ","")
print("White space removed =", white_space_removed)

# print(sentence == white_space_removed)

if white_space_removed == white_space_removed[::-1]:
    print(sentence, "is palindrome")
else:
    print(sentence, "is not a palindrome")
