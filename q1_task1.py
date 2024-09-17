'''
Question 1 - Task 1 requires to extract all 'text' without specifying data formats. 
As CSV file doesn't contain data format, all values can be considered text, thus our Verion 1
We also includes Version 2 to extract only non-numeric values
'''
#VERSION 1 - EXTRACT ALL VALUES
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


#VERSION 2 - EXTRACT ONLY NON-NUMERIC VALUES
import pandas as pd
import numpy as np

# List of CSV file names, specify absolute paths if not stored in same folder
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Output file to be created, specify output path if needed
output_file = 'q1_task1_alltext_nonnumeric.txt'

# Function to check if a value is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Open output file in write mode
with open(output_file, 'w') as f_out:
    # Iterate through each CSV file
    for file in csv_files:
        df = pd.read_csv(file)  # Load CSV file to dataframe
        # Iterate over rows of DataFrame
        for _, row in df.iterrows():
            # Filter out numeric values and join the remaining text values
            text_values = [str(val) for val in row if not is_numeric(str(val))]
            if text_values:
                row_text = ' '.join(text_values)
                f_out.write(row_text + '\n')

print(f"All non-numeric texts have been successfully extracted to {output_file}")
'''
For the purpose of further text analysis in Question 1, we will use the output file of Version 2 'q1_task1_alltext_nonnumeric.text' 
'''