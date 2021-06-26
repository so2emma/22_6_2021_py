usernames = ["Admin", "samuel", "Grace", "samuel", "jacob", "faith"]
new_usernames = ["Grace", "joseph", "peace", "faith"]

for new_username in new_usernames:
    if new_username in usernames:
        print(new_username, " already exists try another")
    else:
        print(new_username, "this username is available")