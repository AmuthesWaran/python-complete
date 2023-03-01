y = int(input('Give me a number '))
count = 0
for x in range(2, y+1, 2):
    print(x)
    count += 1

print(f'we have {count} even numbers')
