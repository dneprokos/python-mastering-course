numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)  # [2, 3, 6, 8, 51]

numbers.sort(reverse=True)  # Will sort in reverse
print(numbers)  # [51, 8, 6, 3, 2]

# Function
newSortedList = sorted(numbers, reverse=True)  # will return a new sorted list
print(newSortedList)

# Sort complex objects
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# It requires to create a function


def sort_item(item):
    return item[1]


# And now we need to pass it as a sorting key
items.sort(key=sort_item)
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
