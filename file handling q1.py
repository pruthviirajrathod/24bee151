import csv

# Data you want to write (list of lists)
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Create a CSV file
filename = "people.csv"

# Open the file in write mode ('w') with newline='' to avoid extra blank lines
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write each row to the file
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully!")
