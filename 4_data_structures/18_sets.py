# Set is a collection without duplicates
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
# Sets are defined in curly bracers
print(uniques)  # {1, 2, 3, 4}


second = {1, 4}
second.add(5)
second.remove(1)
len(second)

# Will return a unique items from both sets
print(uniques | second)  # {1, 2, 3, 4, 5}
# Will return all items present in both sets
print(uniques & second)  # {4}
# Will return the difference in both sets
print(uniques - second)  # {1, 2, 3}
# Will return semnatic difference - Items ether on first set, but not both
print(uniques ^ second)  # {1, 2, 3, 5}

# We cannot access set via index

# But we can use if
if 1 in uniques:
    print("One was found")  # One was found
