"""
Purpose: multiple statements in same line
        , logic seperator
        ; statement completion operator
"""
# in every statement we use this , and ; to se3perator the statement if have multiple lkines

print("hello" "world")
print("hello","world")

print("hello", 21321)
# print("hello" 21321)
# syntaxerror: invalid syntax. perhaps you forget a comma?

print("hello", 213212, 522, 123 -587 +365)
print()

# semi colon seperator

# method 1

num1 = 100
num2 = 300
sum_of_numbers = num1 + num2
print("sum_of_numbers =", sum_of_numbers)

#method 2 using : operator
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2
print("sum_of_numbers:", sum_of_numbers)

"""
pyhton -c "print('hello world')"

python -c "num1 = 123; num2 = 234; sum_of_numbers = num1 + num2; print("sum_of_numbers)

languge
    - scripting language  Ex: batch, shell, etc.....
    - general purpose programing language Ex: c,c++, java,  ect...
    
    python is both scriopting nad general purpose programming language
    
    .bat
        cd directory1
        cd subdirectory2
        ping.google.com > result.txt
"""