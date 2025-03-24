items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# It also requires convertion to list because map returns an object
prices = list(map(lambda item: item[1], items))
print(prices)  # [10, 9, 12]
