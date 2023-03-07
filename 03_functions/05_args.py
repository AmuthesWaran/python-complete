def multiply(*numbers):
    total = 1
    print(f'numbers return a tuples: {numbers}')
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 5, 8))
