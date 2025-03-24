items = [
    ("Product1", 10, True),
    ("Product2", 9, False),
    ("Product3", 12, True),
]

prices = list(map(lambda item: item[1], items))
print(prices)  # [10, 9, 12]
# will produce the same result as previous line
prices = [item[1] for item in items]
print(prices)  # [10, 9, 12]

# Get multiple fields
name_price = [(item[0], item[1]) for item in items]
print(name_price)  # [('Product1', 10), ('Product2', 9), ('Product3', 12)]

filetred_results = list(filter(lambda item: item[1] >= 10, items))
print(filetred_results)  # [('Product1', 10, True), ('Product3', 12, True)]
# will produce the same result as previous line
filetred_results = [item for item in items if item[1] >= 10]
print(filetred_results)  # [('Product1', 10, True), ('Product3', 12, True)]
