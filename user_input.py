student = {}

questioniare = True

while questioniare:
    name = input("\nWhat is your name?")
    room_no = input("What is your room number")

    student[name] = room_no

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        questioniare = False

print("<=========== Data Gathered ==========>")
for name, room_no in student.items():
    print(name + " is in " + room_no + ".")

