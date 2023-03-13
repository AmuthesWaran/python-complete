# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

numbers = [1, 2, 3, 2, 5]
first = set(numbers)
print(first)  # This will remove dups from the list

second = {1, 4}
print(second)
# second.add(5)
# second.remove(5)
# len(second)
union = first | second
print(union)

intersection = first & second
print(intersection)

difference = first - second
print(difference)

symmetric_difference = first ^ second
print(symmetric_difference)
