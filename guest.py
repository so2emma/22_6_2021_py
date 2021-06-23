guest = ["peter", "paul", "samuel"]

print(guest[0] + " is invited to the dinner")
print(guest[1] + " is invited to the dinner")
print(guest[2] + " is invited to the dinner")
print("\n")
print(guest.pop(1).title() + " will not be able to make the dinner")

# replacing the absent person

guest.insert(1, "david")

# second invitation
print("\n")
print(guest[0] + " is invited to the dinner")
print(guest[1] + " is invited to the dinner")
print(guest[2] + " is invited to the dinner")
print("\n")

# adding more people to the list
guest.insert(0, "ope")
guest.insert(2, "emmanuel")
guest.append("frank")

# third invitation
print("\n")
print(guest[0] + " is invited to the dinner")
print(guest[1] + " is invited to the dinner")
print(guest[2] + " is invited to the dinner")
print(guest[3] + " is invited to the dinner")
print(guest[4] + " is invited to the dinner")
print(guest[5] + " is invited to the dinner")
print("\n")

# shrinking the list
print("\n")
print(" sorry can only invite two people ")
print("\n")
print(guest.pop(0).title() + " So sorry cannot invite you to the dinner")
print(guest.pop(0).title() + " So sorry cannot invite you to the dinner")
print(guest.pop(0).title() + " So sorry cannot invite you to the dinner")
print(guest.pop(0).title() + " So sorry cannot invite you to the dinner")

del guest[4]
del guest[5]

print(guest)



