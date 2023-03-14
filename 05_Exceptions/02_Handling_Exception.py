try:
    age = int(input("Age: "))
except ValueError as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))
else:  # else block gets executed only of there are no exception(s)
    print("No exceptions were thrown")

print("Execution continues..")

numbers = [1, 2]
try:
    print(numbers[3])
except IndexError:
    print("given index doesn't exists")

print("Execution continues again...")
