numbers = [10, 0, 7, -1, 3]

# Sort list in ascending order
numbers.sort()
print(numbers)

# Sort list in decending order
numbers.sort(reverse=True)
print(numbers)


# sorted method will return a new list
print(sorted(numbers))

print(sorted(numbers, reverse=True))


items = [
    ("Product1", 10),
    ("Product2", 1),
    ("Product3", 5),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
