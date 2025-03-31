from pathlib import Path

path = Path() / Path("8_python_standard_library") / Path("ecommerce")

# Check if the path exists (True/False)
# path.exists()

# Create the directory 'ecommerce'
# path.mkdir()

# Remove the directory 'ecommerce' (only works if it's empty)
# path.rmdir()

# Rename 'ecommerce' directory to 'ecommerce2'
# path.rename("ecommerce2")

for p in path.iterdir():
    print(p)

# Or
paths = [p for p in path.iterdir()]
# [WindowsPath('8_python_standard_library/ecommerce/contract.py'), WindowsPath('8_python_standard_library/ecommerce/sales'), WindowsPath('8_python_standard_library/ecommerce/__init__.py')]
print(paths)


paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)  # [WindowsPath('8_python_standard_library/ecommerce/sales')]
py_files = [p for p in path.glob("*.py")]
# [WindowsPath('8_python_standard_library/ecommerce/contract.py'), WindowsPath('8_python_standard_library/ecommerce/__init__.py')]
print(py_files)

# Resursive search with rglob
py_files = [p for p in path.rglob("*.py")]
print(py_files)  # [WindowsPath('8_python_standard_library/ecommerce/contract.py'), WindowsPath('8_python_standard_library/ecommerce/__init__.py'), WindowsPath('8_python_standard_library/ecommerce/sales/__init__.py')]
