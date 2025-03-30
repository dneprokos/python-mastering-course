# Run command "python3 "
# __pycache__ will appears in the 7_modules folder
# In this folder we have complied version of modules we imported
# Python verifies the date of compiled file with source and if it is earlier, then it re-compiles


from one_sales import calc_shipping, calc_tax  # Approach 1
import one_sales  # Approach 2

# from one_sales import * - This one considered as bad practice

calc_shipping()
calc_tax()

one_sales.calc_shipping()
