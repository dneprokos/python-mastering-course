try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")  # You didn't enter a valid age.
    print(ex)  # invalid literal for int() with base 10: 'ddss'
    print(type(ex))  # <class 'ValueError'>
else:
    print("This will be run only if there is not exceptions")
print("Execution continues.")
