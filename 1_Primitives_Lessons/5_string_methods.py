course = "Python Programming"
print(course.upper())  # PYTHON PROGRAMMING
print(course.lower())  # python programming
print(course.title())  # Will capitalize first letter of each word
course2 = "   Python Programming   "
print(course2.strip())  # Python Programming
print(course2.rstrip())  # Will remove spaces from the end
print(course.find("pro"))  # Finds an index
course3 = "Python Programming"
print(course3.replace("Pro", "pro"))
print("Pro" in course3)  # Returns boolean
print("Swift" not in course3)  # Will return TRUE
print("43243243".isdigit())  # TRUE
print("43243243")  # TRUE
print("I'm the law".split(' '))  # ["I'm", 'the', 'law']
# ('I could eat ', 'bananas', ' all day')
print("I could eat bananas all day".partition("bananas"))
# For only 49.00 dollars!
print("For only {price:.2f} dollars!".format(price=49))
