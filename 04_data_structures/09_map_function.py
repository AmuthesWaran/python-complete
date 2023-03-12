items = [
    ("Product1", 10),
    ("Product2", 1),
    ("Product3", 5),
]

# Basic method
# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)


# Using Map
#   function declare    iterable
x = map(lambda item: item[1], items)

for item in x:
    print(item)

prices = list(map(lambda item: item[1], items))
print(prices)
