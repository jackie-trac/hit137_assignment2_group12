import pandas as pd

# List of CSV file names, spcecify paths stored somewhere else
csv_files = ['CSV1.csv','CSV2.csv','CSV3.csv','CSV4.csv']

# Output file path
output_file = 'question1_task1_alltext.txt'

# Open the output file in write mode
with open(output_file, 'w') as f_out:
    # Iterate through each CSV file
    for file in csv_files:
        df = pd.read_csv(file)  # Load CSV file to dataframe
        
        # Write the header column names and move to the next line
        f_out.write(','.join(df.columns) + '\n')
        
        # Write each row in the dataframe
        for index, row in df.iterrows():
            # Convert the row to a string and write it to the file
            f_out.write(','.join(row.astype(str)) + '\n')

print(f"All texts have been successfully extracted to {output_file}")
