numbers = [1, 2, 3]


# unpacking one by one
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# unpacking in one go
# Note: len of the list should match the no of variable in the left
first, second, third = numbers

first, second, *others = numbers

print(numbers)
print(others)
print(first)
