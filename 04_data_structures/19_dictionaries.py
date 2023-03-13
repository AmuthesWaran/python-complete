# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

point = {"x": 1, "y": 3}
point2 = dict(x=1, y=2)

print(point)
print(point2)

print(point2["x"])
point2["z"] = 20
print(point2)
