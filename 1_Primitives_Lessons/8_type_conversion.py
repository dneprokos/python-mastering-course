# int(x)
# float(x)
# bool(x)
# str(x)

x = input("x: ")
print(type(x))

y = int(x) + 1
print(f"x: {x}, y: {y}")

# Falsy values in Python
# ""
# 0
# None

# Anything else will be True e.g
bool("False")  # will return True
