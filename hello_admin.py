usernames = ["Admin", "samuel", "Grace", "samuel", "jacob"]
# usernames =[]
if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print("Hello ", username.title(), " would you like to see a status report?\n")
        else:
            print("Hello ", username.title(), " thank you for logging in again\n")
else:
    print("No registered user")
