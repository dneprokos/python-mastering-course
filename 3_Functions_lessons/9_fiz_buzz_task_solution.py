def fiz_buzz(input):
    if not isinstance(input, (int, float)):
        return input

    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fiz"
    elif input % 5 == 0:
        return "buzz"
    return input


print(fiz_buzz(3))
print(fiz_buzz(5))
print(fiz_buzz(15))
print(fiz_buzz(7))
print(fiz_buzz("a"))
print(fiz_buzz(True))
