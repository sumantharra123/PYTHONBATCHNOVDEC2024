"""

purpose: importance of Indentation
"""


print("hello world 1")
  # print("hello world 2")  indentation error: unexpected indent
print("hello world 3")


# block code - if, else, elif, for, while, def, class, ...
# if 12 > 3:
# print('12 is greater than 3')
# indentationerror: expected an indentation block after 'if' statement

if 12 > 3:
    print('12 is greater than 3')


if 12 > 34:
    print("greater")
else:
    print("it is lesser")


if 1 > 2:
    print("case 1")
elif 2 > 1:
    print("case 2")
else:
    print("case 3")


if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print("lesser")
            else:
                print("something")
        else:
            print("something")
    else:
        print("something")


for i in rane (9):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    j = o
    while j < 10:
