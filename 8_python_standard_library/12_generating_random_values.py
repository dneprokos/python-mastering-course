import random
import string


print(random.random())  # Will generate random value between 0 and 1

print(random.randint(1, 10))  # Will generate random value between 1 and 10

print(random.choice([1, 2, 3, 4]))  # Will pick random number from array

# Will return defined number of random numbers
print(random.choices([1, 2, 3, 4], k=2))

letters_and_digits = string.ascii_letters + string.digits
# Get array of 4 chars
print(random.choices(letters_and_digits, k=4))

# Generate a password
print("".join(random.choices(letters_and_digits, k=4)))


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)  # Will shuffle array
