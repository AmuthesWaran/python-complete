list = ["a", "b", "c"]


# Error, Since d is not in the list
print(f"The index of a is {list.index('a')}")

if 'd' in list:
    print(list.index('d'))
