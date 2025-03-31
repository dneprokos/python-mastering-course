from datetime import datetime
import time

dt = datetime(1999, 5, 26)
print(dt)  # 1999-05-26 00:00:00

current_dt = datetime.now()
print(current_dt)  # Will print current date time e.g. 2025-03-31 18:36:48.077316

dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)  # 2018-01-01 00:00:00


dt = datetime.fromtimestamp(time.time())
print(dt)  # Datetime on your machine


# This prints the year and month manually using f-string.
# dt.year gives the year (e.g. 2025), dt.month gives the month number (e.g. 3).
# Output example: 2025/3 (note: month is not zero-padded)
print(f"{dt.year}/{dt.month}")

# This prints the year and month using strftime formatting.
# %Y = 4-digit year, %m = 2-digit month (zero-padded, e.g. 03)
# Output example: 2025/03
print(dt.strftime("%Y/%m"))
