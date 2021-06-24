
# create a list using functions
numbers = list(range(1,6))
print(numbers)

# creating a list of squares
squares = [value**2 for value in range(1,11)]
print(squares)

# creating a list of squares
square = []
for value in range(1,11):
    square.append(value**2)

print(square)
