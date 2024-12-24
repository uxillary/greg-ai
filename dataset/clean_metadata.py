import csv

def clean_text_dataset(input_file, output_file):
    """
    Cleans the text field in a dataset stored as a CSV file.
    Replaces newline characters and double quotes.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned CSV file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()  # Write header to the output file
            for row in reader:
                text = row.get("text", "")  # Get the "text" field
                row["text"] = text.replace('\n', ' ').replace('"', '')  # Clean the text
                writer.writerow(row)  # Write the cleaned row

        print(f"Cleaned dataset saved to {output_file}")
    except Exception as e:
        print(f"Error processing dataset: {e}")

# Replace 'input.csv' and 'output.csv' with your actual file paths
input_file = "metadata.csv"
output_file = "cleaned_metadata.csv"

clean_text_dataset(input_file, output_file)
