items = [
    ("Product1", 10),
    ("Product2", 1),
    ("Product3", 5)
]

# Old way
# filtered = []

# for item in items:
#     if item[1] >= 5:
#         filtered.append(item)

# print(filtered)


# Using filtered method


filtered = list(filter(lambda item: item[1] >= 5, items))
print(filtered)
