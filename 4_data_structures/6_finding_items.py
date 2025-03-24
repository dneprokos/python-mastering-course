letters = ["a", "b", "c"]

print(letters.index("a"))  # 0

# If you will try to search an object that does not exist, in Python it will return an error
# So, it is better to check first
if "d" in letters:
    print(letters.index("d"))
else:
    print("d was not found")

print(letters.count("d"))  # 0


