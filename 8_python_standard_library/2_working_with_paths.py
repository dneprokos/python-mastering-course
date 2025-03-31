from pathlib import Path

# NOTE: Navigate "https://docs.python.org/3/library/pathlib.html" for more info

# Absolute path
Path(r"C:\Program Files\Microsoft")

# Current working directory (relative to where script is run)
Path()

# Relative path to a specific file inside the 'ecommerce' folder
path = Path("ecommerce/__init__.py")

# Joining two paths: current directory + 'Ecommerce' folder
Path() / Path("Ecommerce")

# Builds a relative path: current directory + 'ecommerce' folder + '__init__.py' file
Path() / "ecommerce" / "__init__.py"

# Returns current user home directory
Path.home()

path.exists()
path.is_file()
path.is_dir()
print(path.name)  # __init__.py
print(path.stem)  # __init__
print(path.suffix)  # .py
print(path.parent)  # ecommerce
new_path = path.with_name("file.txt")
print(new_path)  # ecommerce\file.txt
# Gets path absolute value. E.g. c:\PersonalProjects\python-mastering-course\ecommerce\file.txt
print(new_path.absolute())
new_path = path.with_suffix(".cs")
print(new_path)  # ecommerce\__init__.cs
