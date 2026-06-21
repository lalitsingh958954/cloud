## tuple has indexing
# it supports negative indexing as well
# it supports duplicate value
# tuple is immutable data type we can't change data
# tuple is ordered data type
# syntax ()


user_data =("pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","12345","Feb 2nd 2000",5,5,5)

## tuple has indexing result pr
# print(user_data[0])
# print(user_data[-1])
# print(user_data)

## tuple is immutable error 'tuple' object does not support item assignment


# user_data[-1] =0

## if block

user_data1 =("pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","12345","Feb 2nd 2000",5,5,5)
user_data2 =("pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","Feb 2nd 2000",5,5,5.12345)

# it checks position by postion if the values are matching or not

# both are not matching
if user_data1 == user_data2:
    print("both are matching")
else:
    print("both are not matching")


var1 = 5,6

var2 =(10,13)

print(type(var1))

var3, var4 = 8, 9

print(var3)

print(var4)

