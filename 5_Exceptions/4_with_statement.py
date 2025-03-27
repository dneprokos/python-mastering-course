try:
    # with statement automatically release resources
    with open("3_cleaning_up.py") as file, open("another.txt") as another:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("This will be run only if there is not exceptions")
