letters = ["a", "b", "c", "d"]

print(letters[0])  # a
print(letters[-1])  # d

print(letters[0:3])  # ["a", "b", "c"]
print(letters[:])  # copy of original list - ["a", "b", "c", "d"]
print(letters[::2])  # passes a step = ["a", "c"]

numbers = list(range(20))
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1])
