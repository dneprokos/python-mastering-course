from pathlib import Path
import csv

csv_file_name = "data.csv"

# Write to csv file
with open(csv_file_name, "w", newline="") as file:
    writter = csv.writer(file)
    writter.writerow(["transaction_id", "product_id", "price"])
    writter.writerow([1000, 1, 5])
    writter.writerow([1001, 2, 15])

# Read from CSV
with open(csv_file_name) as file:
    reader = csv.reader(file)
    # print(list(reader))  # Will print an arrat of arrays with the lines
    for row in reader:
        print(row)
