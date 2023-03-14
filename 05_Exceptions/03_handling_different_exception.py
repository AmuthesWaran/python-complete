# try:
#     age = int(input("Age: "))
#     xfactor = 10/age
# except ValueError:
#     print("You didn't enter a valid age")
# except ZeroDivisionError:
#     print("Age cannot be 0.")

# else:
#     print("No exceptions were thrown")


try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Enter a valid age")
else:
    print("No exceptions were thrown")
