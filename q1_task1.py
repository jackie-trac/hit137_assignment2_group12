import pandas as pd

# List of CSV file names and paths
csv_files = [
    'D:/Assignment2/CSV1.csv',
    'D:/Assignment2/CSV2.csv',
    'D:/Assignment2/CSV3.csv',
    'D:/Assignment2/CSV4.csv'
]

# Output file path
output_file = 'all_values_text.txt'

# Open the output file in write mode
with open(output_file, 'w') as f_out:
    # Loop through each CSV file
    for file in csv_files:
        df = pd.read_csv(file)  # Load CSV
        
        # Write the header (column names)
        f_out.write(','.join(df.columns) + '\n')
        
        # Write each row in the dataframe
        for index, row in df.iterrows():
            # Convert the row to a string and write it to the file
            f_out.write(','.join(row.astype(str)) + '\n')

print(f"Data has been written successfully to {output_file}")
