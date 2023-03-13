from sys import getsizeof

values = (x * 2 for x in range(1000))
print(type(values))
print("get:", getsizeof(values))
# for x in values:
#     print(x)


values = [x * 2 for x in range(1000)]
print(type(values))
print("list:", getsizeof(values))
