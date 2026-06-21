Type Casting 21st June python list data type
#
# i = 5
# j = "1"
#
# print("sum of i and j is", i + int(j))

# user_data =["pr", "reddy","123","pr@gmail.com","12345","Feb 2nd 2000",5]

# print(user_data)
# print(user_data[0]) #pr
# print(user_data[-5]) #123

# print(user_data[0].upper())
# print(user_data)

## list is mutable means

# user_data[0] = user_data[0].upper()  ##by this can change list
# print(user_data)

# change the string test mutable

# name = "Reddy"
#
# print(name)
#
# name [1] = "r"




# user_data.pop()  ## it will delete the last value

# user_data.pop(-4)  ## it will delete mail id if both are used it will give prioriy to pop 105 line
#
# print(user_data)

# user_data.append("lalit")  # it will add a new line at the last
# print(user_data)
# user_data =["pr", "reddy","123","pr@gmail.com","12345","Feb 2nd 2000",5]
# # user_data.insert(1,"new key")  ## it will update new value at 1 place
# user_data.insert(-3,"new last key")  ## it will give new value before -3

##  ['pr', 'reddy', '123', 'pr@gmail.com', 'new last key', '12345', 'Feb 2nd 2000', 5]


# print(user_data)

# name = "Reddy"  # string is immutable so it will not change the name
#
# name.upper()
#
# print(name) # string is immutable so it will not change the name and result is same after changing it to upper

#
# name = "Reddy"
#
# name = name.lower()   ## it will change means new value then only we can see as string is immutable and list is mutable
# #so we can change the list value by append here it will removed the address of name in first and give in second lower
# print(name)

# user_data =["pr", "reddy","123","pr@gmail.com","12345","Feb 2nd 2000","5"]
# #
# # # user_data.reverse()
# #
# #
# # print(len(user_data))  # to get how many no. of element in list available

# name = "PR Reddy"
#
# # print(name.split())  ## it will by default  space is delimiter split it according to space and give 2 element like
# # ['PR', 'Reddy']
#
# print(name.split("e"))  # it will split by e ['PR R', 'ddy']

## print empty string

# user_data =["pr", "reddy"," ", "123","pr@gmail.com","12345","Feb 2nd 2000",5]
#
# print(user_data)

# user_data =["pr", "reddy"," ", "123",["pr@gmail.com", "reddy@gmail.com"],"12345","Feb 2nd 2000",5]
# user_data[4].insert(0,"new@gmail.com")  ## to update mail id at 0th place
# print(user_data)







