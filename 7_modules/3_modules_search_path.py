# When python sees it, it looks for "one_sales.py" file in the current directory
import one_sales
import sys

# If it didn't find it, it will start search in a list of predefined directories
print(sys.path)  # Will show all of the directories list

