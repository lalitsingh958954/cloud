# def add(a,b):
#     print("address of a=", id(a))
#     return a + b
#
#
# result = add(1,1)
# print("result is ", result)
# if the function is inside the class is called method outside it is called function
# to call method we need to call by object by calling class
# in obj1 it is allocating some memory location where the data gets stored
# self will collect object memory location
# memory location for obj1 and obj2
# obj1 = Calculater()
# print(obj1)
# <__main__.Calculater object at 0x000001AFAB41B4D0>
# <__main__.Calculater object at 0x000001AFAB41E350>
# __init__ id used when i want to use the later
# self is here the address location for obj1 address of obj1 will be collected by this self
# other value are collected by the positional argument



# def sub():
#     return a -b

#
# class Calculater:
#     def add(self,a, b):
#         print(self)
#         return a + b

# obj1 = Calculater()
# print(obj1)
# #
# obj2 = Calculater()
# print(obj2)
#
# result = obj1.add(1,1)
# print("result =", result)
# # result = add(2,3)
#
# result = obj2.add(4,8)
# print("result =", result)


class Calculator:
    def __init__(self,num1,num2):
       self.num1 = num1  # when obj1 is calling the value of num1 is self address location and num1
       self.num2= num2


    def add(self): #    #Create a method that works with the current object.
        return self.num1+self.num2  # Read num1 and num2 stored in that object and return their sum.


    def sub(self):
        return self.num1-self.num2

obj1 = Calculator(1,2)
obj2 = Calculator(4,3)

print(obj1.add())
print(obj2.sub())









