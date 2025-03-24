def fizz_buzz(input):
    if isinstance(input, bool) or not isinstance(input, int):
        return input
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    return input


# Test cases
print(fizz_buzz(3))   # fizz
print(fizz_buzz(5))   # buzz
print(fizz_buzz(15))  # fizzbuzz
print(fizz_buzz(7))   # 7
print(fizz_buzz(0))   # fizzbuzz
print(fizz_buzz(-3))  # fizz
print(fizz_buzz("a"))  # "a"
print(fizz_buzz(True))  # True
print(fizz_buzz(3.0))  # 3.0
