# creating a dictionary
color = {'sky': 'blue', 'grass': 'green', 'fire': 'red', 'snow': 'white'}
# accessing values in a dictionary
print(color['sky'])
# adding to a dictionary
color['chair'] = 'brown'
# modifying values in a dictionary
color['fire'] = 'blue'
# deleting values from a dictionary
del color['sky']

# looping through a dictionary
for key, value in color.items():
    print("\n key: " + key)
    print("\n value: " + value)
