"""
purpose: print() function syntax and usage
"""

name = "almighty"  # str

print("name =", name)
print("name of a student is name")

#     str         str

print("name of the student is" + name)
print("name of the student is " + name)
print()

print("name of the student is", name)
print("name of the student is", name, sep=" ")
print("name of the student is", name, sep="_")
print("name of the student is", name, sep=":")

print(1, 2, 3, 4, 5, 6,)  # default sep=' '
print(1, 2, 3, 4, 5, 6, sep=" ")
print()


print(1, 2, 3, 4, 5, 6,  sep= "!")
print(1, 2, 3, 4, 5, 6,  sep= ":")
print(1, 2, 3, 4, 5, 6,  sep= "_")
print()


# note: Python is a Dynamic typed language
name = 1232
print("name of the student is", name)

##                    string                 int

# print('name of the student is',+ name)
# typeerror: can only concentrate str

# Note: python is strictly typed language

print("1 + 2      =",  +   2)  # adition
print("'1' + '2'    =", "1" + "2")  # string  concatination
print()

# 1 + '2' # TypreError: unsported operand type(s) for +: 'int' and 'str'
# type converters - str(), int(), float()
print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")

print()
print("int('234')  +", int("234"))

# print("int('23.4')  =", int('23.4'))  # ValueError: invalid literal for int
# print("int('two')  =", int('two')) # valueerror: invalid literal for int


print("name of the student is" + str(name))
print("name of the student is" + " " + str(name))