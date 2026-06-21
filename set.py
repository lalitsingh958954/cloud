## set data collection
## set is immutable data type
## set by default remove duplicate value
## set is not following any index no.
## set is unordered

## {} syntex

# user_data ={"pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","12345","Feb 2nd 2000",5,5,5,}

# print(type(user_data))  ## check the type <class 'set'>
# ## here we use curly braces it is called set
#
# print(user_data[0])  ## set is not following any index no.

# print(user_data)  ## set by default delete duplicate value

## input  user_data ={"pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","12345","Feb 2nd 2000",5,5,5,}

## output {5, '12345', 'pr@gmail.com', 'pr', 'Feb 2nd 2000', 'reddy@gmail.com', ' ', '123', 'reddy'}

# # set data collection is unordered data type  as in input see tha output you see any value is coming
#
# user_data ={"pr", "reddy"," ", "123","pr@gmail.com", "reddy@gmail.com","12345","Feb 2nd 2000",5,5,5,}
#
# # user_data[3] = "333"  ## we can't change as set is immutable

user_data1 ={"pr", "reddy" ,"999","pr@gmail.com", "12345","Feb 2nd 2000",5,5,5}
user_data2 ={"pr", "reddy","pr@gmail.com", "12345","Feb 2nd 2000",5,"999"}

# it checks position by postion if the values are matching or not
# both are matching because set is not matching index by index, it checks if data is there or not in both cases
# doesn't matter data in which position
# since it is removing the duplication it is not considering the 5,5 into the comparision as all 5 3 times will be
# calculated as one time
if user_data1 == user_data2:
    print("both are matching")
else:
    print("both are not matching")


