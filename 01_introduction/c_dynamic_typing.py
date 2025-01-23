num1 =  200
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num 1", num1)
print("num1 = ", num1)

# works in both static and dynamic typing
num1 = 300
print("num1 =", num1, "type =", type(num1)) #int


# python is a dynamic typed language
num1 = 300.0
print("num1 =", num1, "type =", type(num1))

num1 = 300.
print("num1 =", num1, "type =", type(num1))

num1 = 300, # tuple(data structure)
print("num1 =", num1, "type =", type(num1))

num1 = (300,)
print("num1 =", num1, "type =", type(num1))

num1 = -0.09
print("num1 =", num1, "type =", type(num1))

num1 = -0.09j
print("num1 =", num1, "type =", type(num1))
print()

num1 = "300"
print("num1 =", num1, "type =", type(num1))

num1 = "three"
print("num1 =", num1, "type =", type(num1))

num1 = True
#num1 = true
print("num1 =", num1, "type =", type(num1))

num1 = False
print("num1 =", num1, "type =", type(num1))

num1 = None
print("num1 =", num1, "type =", type(num1))

num1 = "NONE"
print("num1 =", num1, "type =", type(num1))

num1 = "none"
print("num1 =", num1, "type =", type(num1))

# NOTE: Strings need to be declared in quotes