import pandas as pd

# List of CSV file names, specify absolute paths if not stored in same folder
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Output file to be created, specify output path if needed
output_file = 'q1_task1_alltext.txt'

# Open output file in write mode
with open(output_file, 'w') as f_out:
    # Iterate through each CSV file
    for file in csv_files:
        df = pd.read_csv(file)  # Load CSV file to dataframe
        # Iterate over rows of DataFrame
        for _, row in df.iterrows():
            # Convert each row to a string with space-separated values
            row_text = ' '.join(row.astype(str).values)
            f_out.write(row_text + '\n')
#As CSV files do not contain data format, all values are considered as 'text'
print(f"All texts have been successfully extracted to {output_file}")