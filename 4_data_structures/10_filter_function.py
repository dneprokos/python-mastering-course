items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filetred_results = list(filter(lambda item: item[1] >= 10, items))
print(filetred_results)  # [('Product1', 10), ('Product3', 12)]
