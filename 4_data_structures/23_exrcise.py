from pprint import pprint

# Find the most repeated character in this text
sentence = "This is a common interview question"

chars_frequency = {}

for char in sentence:
    if char in chars_frequency:
        chars_frequency[char] += 1
    else:
        chars_frequency[char] = 1
# {'T': 1, 'h': 1, 'i': 5, 's': 3, ' ': 5, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1, 'w': 1, 'q': 1, 'u': 1}
print(chars_frequency)
pprint(chars_frequency, width=1)
# {' ': 5,
#  'T': 1,
#  'a': 1,
#  'c': 1,
#  'e': 3,
#  'h': 1,
#  'i': 5,
#  'm': 2,
#  'n': 3,
#  'o': 3,
#  'q': 1,
#  'r': 1,
#  's': 3,
#  't': 2,
#  'u': 1,
#  'v': 1,
#  'w': 1}


# Convert to lust of tuples and sort
char_frequency_sorted = sorted(
    chars_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])  # ('i', 5)
