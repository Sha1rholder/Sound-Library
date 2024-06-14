import csv

file_path = "./data/over-ear sensitivity official.csv"

# Open the original CSV file in read mode and a new file in write mode
with open(file_path, mode="r", newline="", encoding="utf-8") as infile, open(
    file_path, mode="w", newline="", encoding="utf-8"
) as outfile:
    # Create a CSV reader and writer
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header (first row) from the input file
    header = next(reader)
    # Insert the new column name 'production' between 'back' and 'note'
    header.insert(8, "production")
    # Write the updated header to the output file
    writer.writerow(header)

    # Iterate over each row in the original CSV
    for row in reader:
        # Insert 'in production' in the new column for each row
        row.insert(8, "producing")
        # Write the updated row to the output file
        writer.writerow(row)
