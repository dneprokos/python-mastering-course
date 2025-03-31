from pathlib import Path
from zipfile import ZipFile

ecom_path = Path() / "8_python_standard_library" / "ecommerce"
zip_file_name = "files.zip"

# Create a zip file and put everything from 8_python_standard_library/ecommerce
with ZipFile(zip_file_name, "w") as zipFile:
    for path in ecom_path.rglob("*.*"):
        zipFile.write(path)

with ZipFile(zip_file_name) as zip:
    file_names = zip.namelist()
    print(file_names)  # Will return name of all the files in zip
    info = zip.getinfo(file_names[1])
    print(info)  # <ZipInfo filename='8_python_standard_library/ecommerce/__init__.py' filemode='-rw-rw-rw-' file_size=45>
    zip.extractall("zip_extracted_files")
