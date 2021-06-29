courses = {
    'specific': ["CSC 221", "CSC224", "CSC 225", "CSC 226", "CSC 227"],
    'General': ["GST 221", "GST 222", "TMC 221", "EDS 221"]
}
for type, codes in courses.items():
    print("Type: " + type)
    for code in codes:
        print("Course code: " + code)

# popping a list in a dictionary
courses['specific'].pop()
print("Hope this works", courses['specific'])

# A hall hierarchy system
paul = {
    'C 100': {
        'c101': ["james", "Samuel", "Micheal", "Jacob", "John", "judge"],
        'c102': ["james", "Samuel", "Micheal", "Jacob", "John", "judge"]
    }
}
for hall, floor in paul.items():
    print("Haul: " + hall)
    for floors, rooms in paul['C 100'].items():
        print("Floor: " + floors)
        for room in rooms:
            print("Member: " + room)
