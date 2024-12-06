""" 
#purpose: print() fnction syntax and usage
    escape sequences
        - characters whose presence is felt, but they are not seperated
       \t - tab space 
       \n - new line 
       \b - owerwrites prewvious character

        r'' raw string 


"""

print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")


print()
# to ignore the escape sequesces
print("hello \tworld \npython")
print(r"hello \tworld \npython")

print("C:\my\newfolder") # noqa: w605
print(r"C:\my\newfolder")
print()


# --------------------
# print(data, sep=' ', end = '\n')

print("hello")  # default end ='\n'
print("world")

print("hello", end="\n")
print("world", end="\n")

print("helllo", end="_____")
print("world")   # ddefault end='\n' 

print("helllo", end="\t")
print("world")   # ddefault end='\n' 

print("hello", "python", "12312", end="\t")
print("world")


print("i am a hero", "my name is sumanth", end="\n")
print("hero")

print("hello", "python", "12312", end="\t", sep=";")
print("world")


