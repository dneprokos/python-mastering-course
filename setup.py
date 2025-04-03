import setuptools
from pathlib import Path

setuptools.setup(
    name="{unique_package_name}".
    version={package_version},
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["package_to_exclude"])
)
