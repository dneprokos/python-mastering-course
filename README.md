# Complete Python Mastering

![main image](/images/python_main.png)

This project was designed based on Complete Python Mastery course from Mosh Hamedani. The goal of this project is to refresh a memory about Python programming langauge

## Preconditions

### Python installation

1. Python 3 should be installed - https://www.python.org/downloads/

Note: Please don't forget to include it to the environment variables path

### IDE or Editor installation

#### PyCharm

Option a is to install PyCharm - The Python IDE for data and web professionals https://www.jetbrains.com/pycharm/. The problem is it is not a free

#### Visual Studio Code with extensions

Visual Studio Code is fully free and you can make extension installations in order to make this editor very close to IDE

- Visual Studio Code - https://code.visualstudio.com/

Recommended Extensions

- autopep8
- Python

## How to run the program

### Run from command line

- Open command line and run "python <file_path>.py" e.g. "python .\1_Primitives_Lessons\8_type_conversion.py"

### Run from Visual Studio Code (requires Python extension)

- Python extension should be installed
- Click "Run Code" button on the right-top corner of the screen

![run code image](/images/run_code.png)

## Work with PIPENV

Pipenv is a tool for managing Python projects. It combines package management (like pip) and virtual environments (like venv) into one streamlined workflow.

Key features:

- Automatically creates and manages a virtual environment.

- Uses a Pipfile and Pipfile.lock instead of requirements.txt to track dependencies.

- Ensures consistent environments across machines.

- Makes dependency resolution easier and more secure.

In short: Pipenv simplifies installing, managing, and locking Python project dependencies.

### Useful commands

- Get Virtual environment location

`pipenv --venv`

- Install dependencies

`pipenv install`

- Install dependencies from Pipfile.lock instead of Pipfile

`pipenv install --ignore-pipfile`

- Activate virtual environment

`pipenv shell`

- Diactivate virtual environment

`exit`

- See the list of all installed dependencies

`pipenv graph`

- Uninstall some package

`pipenv uninstall <package_name>`

- Install specific version of the package

`pipenv install <package_name>=<package_version>`

- Find outdated packages

`pipenv update --oudated`

- Update specific package

`pipenv update <package_name>`

### Publishing packages

- Account should be created for "https://pypi.org/"
- Install packages on your local machine

`pip install setuptools wheel twine`

- As a best practice, create a directory with a package name

- Create an "**init**.py" in this directory

- Next you can add a modules with the logic

- Create a "setup.py" file in the root of the project

<pre>
import setuptools
from pathlib import Path

setuptools.setup(
    name="{unique_package_name}".
    version={package_version},
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["package_to_exclude"])
)
</pre>

- Create "README.md" file with package description
- Create a license file. You can get a template from "https://choosealicense.com/"
- Create a distribution files with a command

`python setup.py sdist bdist_wheel`

, It will generate 'build' and 'dist' folders

- Use twine to upload distribution
  `twine upload dist/*`

  ,It will ask for username and password

- Verify package on the "https://pypi.org/"

## Pydoc

Using pydoc is a great way to view documentation for Python modules, classes, functions, and more — directly from the terminal or by generating HTML pages. Here's a quick guide:

- Run in the terminal
  `pydoc <module_or_function>`
