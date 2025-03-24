items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort(key=lambda item: item[1])
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
