import sys

# sys.argv is a list of command-line arguments passed to the script when you run it.
print(sys.argv)

if (len(sys.argv) == 1):
    print("USAGEL python 16_command_line_arguments.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# NOTE: Type "python .\8_python_standard_library\16_command_line_arguments.py 123" in CMD in you will receive a "Password 123"
