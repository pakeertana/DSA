#single line
num=6
for i in range(num):
    print("*")

#
num=6
for i in range(num):
    print("*"*i)

#
num=6
for i in range(num):
    print(" "*(num-i-1),"*"*i)

#
num=6
for i in range(num):
    print(" "*(num-i-1),"*"*(2*i+1))

#
num=10
for i in range(num):
    print("*"*num)

#
num=10
for i in range(num):
    print("*"*(i+1))


#
num=10
for i in range(num):
    count=num-i
    print("*"*count)

#
num = 10
for i in range(num):
    count = num - i
    print(' ' * i + "*" * count)


#
num = 10
for i in range(num):
    count = num - i
    print(' ' * count + "*" * (i + 1))


#
num = 10
for i in range(num):
    count = num - i
    print(' ' * (count // 2) + "*" * (i + 1))