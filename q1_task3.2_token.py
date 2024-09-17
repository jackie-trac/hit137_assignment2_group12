'''
Question 1 - Task 3.2 requires to count unique tokens and give top 30 words.
Since tokens can be special characters, sub-words and nonwords this version of code takes into account all tokens.  
'''
#VERSION 1 - TOP 30 UNIQUE TOKENS
from transformers import AutoTokenizer
from collections import Counter
import csv
import warnings

# Define a function to flexible adjust input/output file, show processing progress for large file
def process_file_with_tokens(text_file, output_csv, model_name="bert-base-uncased", chunk_size=1000):
    # Suppress the FutureWarning
    warnings.filterwarnings("ignore", category=FutureWarning)

    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, clean_up_tokenization_spaces=True)

    # Initialize a Counter to keep track of token frequencies
    token_counts = Counter()

    # Get the total file size for progress tracking
    total_size = 0
    with open(text_file, 'r', encoding='utf-8') as f_in:
        f_in.seek(0, 2)  # Move to the end of the file
        total_size = f_in.tell()  # Get the total size of the file
        f_in.seek(0)  # Return to the beginning of the file

        processed_size = 0  # Track how much of the file has been processed
        while True:
            # Read the file in chunks
            chunk = f_in.read(chunk_size)
            if not chunk:
                break

            # Tokenize the chunk, truncating to max length
            tokens = tokenizer.tokenize(chunk)[:tokenizer.model_max_length]

            # Update the token counts (including all tokens)
            token_counts.update(tokens)

            # Calculate and display the progress percentage
            processed_size += len(chunk)
            progress_percentage = (processed_size / total_size) * 100
            print(f"Processing: {progress_percentage:.2f}% complete", end='\r')

    print("\nProcessing complete!")

    # Extract the 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    # Write the 30 most common tokens to the output CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Token', 'Count'])  # Write the header row
        csvwriter.writerows(top_30_tokens)  # Write the token counts

    # Confirmation message when the process is done
    print(f"30 most common tokens have been extracted to {output_csv}")

if __name__ == "__main__":
    text_file = 'q1_task1_alltext_nonnumeric.txt'  # Path to the input text file
    output_csv = 'top_30_tokens_transformers.csv'  # Path to the output CSV file
    process_file_with_tokens(text_file, output_csv)
