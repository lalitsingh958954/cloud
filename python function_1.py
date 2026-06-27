# Login app
# Database
# Input
# user validation
# password validation
import string

#database
# def reg():
registration ={
        'user1':{ "login_name" : "pr", "password": 123},
        "user2":{"login_name" : "rj", "password": "rj123"},
        "user3":{ "login_name" : "ar", "password": "ar123"}
        }

#login functionality
def login(x: string, y: int):
    for user in registration:
        if x == registration[user]["login_name"]:
            print("user found in database")
            if y == registration[user]["password"]:
                print("password match")
            else:
                print("password is not matched login failed")
            break
        else:
            continue

# input
def main():
    user_name = input("Enter your username: ")
    user_password = input("enter password: ")
    login(user_name, int(user_password))  ## call by value

    ## we need to use type casting her in line 32 as we have given value as int in line no. registeration 10 line



# reg()
main()


