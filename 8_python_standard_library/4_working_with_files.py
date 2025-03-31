from pathlib import Path
from time import ctime
import shutil

# Build path to '8_python_standard_library/ecommerce'
path = Path() / "8_python_standard_library" / "ecommerce" / "__init__.py"
print(path)

# Check if the path exists (BUT you're not printing or using the result)
# path.exists()

# Rename 'ecommerce' to 'init.txt'
# ⚠️ Will raise error if 'ecommerce' is a directory and 'init.txt' exists
# path.rename("init.txt")

# Delete the path (file or empty folder)
# path.unlink()  # ⚠️ Will raise error if it's a directory — only works for files

# Get file stats
stat_result = path.stat()  # ⚠️ Will raise error if the file/path no longer exists
print(stat_result)
print(ctime(path.stat().st_ctime))  # Sun Mar 30 15:03:12 2025

file_bytes = path.read_bytes()
print(file_bytes)  # Ecommerce  package was initialized"
# path.write_text("...") Will write text to the file


# shutil.copy("source_location", "target_location")
