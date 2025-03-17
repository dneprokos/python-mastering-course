message = "a"  # global variable


def greet(name):
    message = "b"  # local variable. Will be garbage collected after method is used


print(message)  # Will print a. Because it seeing only global in this case
