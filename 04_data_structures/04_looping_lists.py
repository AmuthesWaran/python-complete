letters = ["a", "b", "c"]
for letter in letters:
    print(letter)


for letter in enumerate(letters):
    print(letter)  # This returns a tuples with index and item with that index

for index, letter in enumerate(letters):
    # To unpack a tuple
    print(index, letter)


for letter in enumerate(letters):
    print(letter[0])
