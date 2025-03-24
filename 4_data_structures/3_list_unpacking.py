numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]

# numbers of var should be the same as number of elemenents
first, second, third = numbers
print(first)  # 1

one, two, *other = numbers

print(one)  # 1
print(other)  # [3]

first, *other, last = numbers
print(first)  # 1
print(last)  # 3
