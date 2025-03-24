letters = ["a", "b", "c"]


# Add
letters.append("d")
print(letters)  # ["a", "b", "c", "d"]

# Insert anywhere
letters.insert(0, "-")
print(letters)  # ['-', 'a', 'b', 'c', 'd']

# Remove
letters.pop()  # Removes last
print(letters)  # ['-', 'a', 'b', 'c']

letters.pop(-1)  # Removes for specific index. Last in this case
print(letters)  # ['-', 'a', 'b']

letters.remove("b")  # Will remove a first accurance
print(letters)  # ['-', 'a']

del letters[0:-1]  # will delete items by specified indexes range
print(letters)  # ['a']

letters.clear()  # fully clears
print(letters)  # []
