from array import array

numbers = array("i", [1, 2, 3])
print(type(numbers))

numbers.append(4)
numbers.insert(5, 4)
# numbers.pop()
# numbers.remove()
print(numbers)
