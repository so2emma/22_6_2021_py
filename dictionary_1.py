# Exercise 1 { person ] ========================================>
person = {
    'first_name': "Oso", 'last_name': 'Emmanuel', 'age': '18', 'city': 'Lagos'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# Exercise 2 { Favourite Numbers } =============================>
for key, values in person.items():
    print("key: ", key)
    print("value: ", values)
