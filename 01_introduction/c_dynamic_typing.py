"""

purpose: python is a dynamic typed language.
    programming languages
        - classification
            1. static - typed languages
                - first declare the variables, &
                - then use them
                    int a, float b  # Declaration
                    a = 10          # initialization

            2. dynamic typed languages
                - create when you need. No declaration needed
                num1 = 123

    python code  --> pyhton byte code  -> python interpretor  ->  c compiler ->  machine
    so, python is slower compared to compailer based languages
"""


num1 = 100
type(num1)

print(type(num1))

print(num1)
print("num1")

print("num1", num1)
print("num1 =", num1)

print("num1 =", num1, "type =", type(num1))



# works in both static and dynamic typing

num1 = 300
print("num1 =", num1, "type =", type(num1))  #int

# python is a dynamic-typed language
num1 = 300.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = 300.
print("num1 =", num1, "type =", type(num1))  # float


num1 = 300,
print("num1 =", num1, "type =", type(num1))  # tuple

num1 = (300,)
print("num1 =", num1, "type =", type(num1))  # tuple

print()

num1 = 300.0
print("num1 =", num1, "type =", type(num1))  # float

num1 = -0.99
print("num1 =", num1, "type =", type(num1))  # float


num1 = -0.99j
print("num1 =", num1, "type =", type(num1))  # complex
print()

num1 = "300"
print("num1 =", num1, "type =", type(num1))  # string
print()

num1 = True
# num1 = true  # python is a case sensitive language
print("num1 =", num1, "type =", type(num1))

num1 = False
print("num1 =", num1, "type =", type(num1))  #bool

num1 = None
print("num1 =", num1, "type =", type(num1))  # none

num1 = "None"
print("num1 =", num1, "type =", type(num1)) # string

num1 = "none"
print("num1 =", num1, "type =", type(num1))  # string

# Note:  strings need to be declared in quotes