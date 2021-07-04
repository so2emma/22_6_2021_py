# PART 1
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print('\nUsernames: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\nFullname: ' + full_name.title())
    print('\nLocation: ' + location.title())

# PART 2
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print("Verifying user: " + current_users.title())
    confirmed_users.append(current_users)
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())