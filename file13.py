import json
import csv

# Read JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)   # loads JSON array

# Write to CSV file
with open("output.csv", "w", newline="") as csv_file:
    
    # Get headers from JSON keys
    headers = data[0].keys()
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    
    writer.writeheader()   # Write column names
    writer.writerows(data) # Write data rows

print("JSON data successfully converted to CSV.")