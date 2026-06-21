# if we need data in key and value
# key will always be in quoted marks
# value can be string or int
# if value has " marks then it will be treated as string if int no string required
# it does not have any indexing
# we can get the value by key name
# dictonary is unordered data type
# dictonary is mutable





# print(user_data1)

# getting value by key name

# print(user_data1["last_name"])
#
# #both are matching
# user_data1 ={"first_name":"pr","last_name":"rdydddd","mob_no":"999","email":"pr@gmail.com","number":12345}
# user_data2 ={"first_name":"pr","mob_no":"999","email":"pr@gmail.com","number":12345,"last_name":"rdydddd"}
#
# if user_data1 == user_data2:
#     print("both are matching")
# else:
#     print("both are not matching")

user_data1 ={"first_name":"pr","last_name":"rdydddd","mob_no":"999","email":"pr@gmail.com","number":12345}

# user_data1['first_name'] = "AR"

# print(user_data1.keys())  # it will give keys
#dict_keys(['first_name', 'last_name', 'mob_no', 'email', 'number'])

# print(user_data1.values()) # it will give values
# (.venv) PS C:\Users\hp\Desktop\python> python3 .\dictonary.py
# dict_values(['pr', 'rdydddd', '999', 'pr@gmail.com', 12345])

# print(user_data1.items())  # it will give key and values
#(.venv) PS C:\Users\hp\Desktop\python> python3 .\dictonary.py
#dict_items([('first_name', 'pr'), ('last_name', 'rdydddd'), ('mob_no', '999'), ('email', 'pr@gmail.com'), ('number', 12345)])

# key value pair is extracted as tuple format
#
# user_data1 ={"first_name":"pr","last_name":"rdydddd","mob_no":"999","email":"pr@gmail.com","number":12345}
#
# # control statement for loop
#
# # for key,value in user_data1.items():
# #     print(f"{key},{value}")
#
#     # result
#
#     # first_name, pr
#     # last_name, rdydddd
#     # mob_no, 999
#     # email, pr @ gmail.com
#     # number, 12345
# user_data1 = {"first_name": "pr", "last_name": "rdydddd", "mob_no": "999", "email": "pr@gmail.com", "number": 12345}
#
# for i in user_data1.values():
#     print(f"{i}")


# ## it will give values
# pr
# rdydddd
# 999
# pr@gmail.com
# 12345
