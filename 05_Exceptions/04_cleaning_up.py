try:
    file = open("content.txt")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you didnt enter a valid age")
else:
    print("No Exception were thrown")
finally:
    file.close()
