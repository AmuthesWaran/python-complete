try:
    # opening file with with statement will close the file without calling .close()
    with open("content.txt") as file:
        print("File Opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didnt enter a valid age")
else:
    print("No Exception were thrown")


# if an object has magic methods like __enter__ and __exit__ then we can make use of with statement (Context management protocol)
# file.__enter__
