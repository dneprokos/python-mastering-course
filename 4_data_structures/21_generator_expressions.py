from sys import getsizeof

values = (x * 2 for x in range(1000))  # Values will be a generator object
print(type(values))  # <class 'generator'>
print("gen:", getsizeof(values))  # gen: 112
