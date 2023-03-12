items = [
    ("Product1", 10),
    ("Product2", 1),
    ("Product3", 5)
]


# List Comprehensions
# [expression for item in items]
list_of_all_prices = [item for item in items]
list_of_prices_greater_than_or_equal_to_five = [
    item for item in items if item[1] >= 5]

print(list_of_all_prices)
print(list_of_prices_greater_than_or_equal_to_five)
