letters = ["a", "b", "c", "d"]
print(letters)


# Add
letters.append("e")
print(letters)


letters.insert(0, "*")  # Inserts item to the given index
print(letters)


# Remove
letters.pop()  # Removes last index
print(letters)

letters.pop(0)  # Removes the given index
print(letters)

letters.remove("c")  # Removes 1st occurence of the "c" in the list
print(letters)

del letters[0]
# Deletes item based on its index, same goes for range of index as well [0:3], [:3]
print(letters)


letters.clear()  # To remove all the items in the list
print(letters)
