message = 'This is a single line message'

message2 = "This is a another single line message"

message3 = '''This is a another 
multi-line line message'''

message4 = "This is a another \n multi line message using \\n"

print(len(message3))

print(message2)

name = 'Ammu'

# String Concatination
message5 = 'Hello, ' + name
print(message5)


message6 = 'Hello, {}'.format(name)
print(message6)


message7 = f'Hello, {name}'
print(message7)

# Note: f-string wont work on python lower than 3.6


print(message7.upper())
print(message7.lower())
print(message7.capitalize())
print(message7.title())
print(message7.swapcase())
print(message7.replace('Hello', 'Hi'))

message8 = input('What day is today?').strip()
print(message8)
