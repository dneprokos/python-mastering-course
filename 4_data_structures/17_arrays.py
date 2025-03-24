from array import array

# As first paramter we specify a type. If we defined type, we should always use it
numbers = array("i", [1, 2, 3])
print(numbers)  # array('i', [1, 2, 3])

numbers.append(4)
