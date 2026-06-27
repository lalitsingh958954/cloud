##  function
# we can't give more argument which are there in function so we will get error
# when caller is giving more argument than the function then we will use
# def calc(**kwargs) key word arguments and that will be collected in dictonary format
# key can not be same value can be same in dictonary


# def calc(num1, num2):
#     print(num1)
#     print(num2)
#
# #calc(1,2,3)

#
# def calc2(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# calc2(num1=10,num2=20,num3=30)

# output

# num1 10
# num2 20
# num3 30

# def calc2(**kwargs):
#     print(kwargs)
#
# calc2(num1=10,num2=20,num3=30)

# output
# {'num1': 10, 'num2': 20, 'num3': 30}


#
# def calc2(**kwargs):
#     print(kwargs)
#
# calc2(num1=10,num2=20,num3=20)

# *kwargs value will be captured in list format

# def calc2(*kwargs):
#     print(kwargs)
#
# calc2(10,20)
#
# output
#
# (10, 20)

# def calc2(*kwargs):
#     for i in kwargs:
#         print(i)
#
# calc2(10,20)
#
# output
#
# 10
# 20


# numbers = [10,20,30]
# name = "lalit"
#
# def myfun():  ## call by value
#     return name.upper()
#
# def no(a):  ## call by reference
#     numbers.append(a)
#     return numbers
#
# myfun()
# no(5)
#
# b=myfun()
# print("my name",b)
# print(numbers)
#
# output
#
# my name LALIT
# [10, 20, 30, 5]




