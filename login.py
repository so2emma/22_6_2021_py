# first_name = input("Enter Firstname: ")
# last_name = input("Enter Lastname: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

details = {'atom': 'emmanuel', username: password}

# Username confirmation
username_2 = input("Confirm Username: ")

for user in details:
    if user == username:
        print("Your username is correct. ")
        # Password confirmation
        password_2 = input("Confirm Password: ")
        if password_2 == details[user]:
            print("you have logged in finally")
        else:
            print(" incorrect Password")
    else:
        print("Incorrect username.")
