try:
    file = open("3_cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("This will be run only if there is not exceptions")
finally:
    file.close()
