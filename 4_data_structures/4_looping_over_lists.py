letters = ["a", "b", "c", "d"]

for leter in letters:
    print(leter)  # a b c d

# returns tuple of index and value
for leter in enumerate(letters):
    print(leter[0], leter[1])
    # 0 a
    # 1 b
    # 2 c
    # 3 d

# Simplification - Unpacking tuple
for index, leter in enumerate(letters):
    print(index, leter)
    # 0 a
    # 1 b
    # 2 c
    # 3 d
