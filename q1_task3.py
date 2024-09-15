from collections import Counter
import re
import csv

# Define a function to flexible adjust input/output file, show processing progress for large file
def process_file(text_file, output_csv, chunk_size=16384):
    # Initialize a Counter to keep track of word frequencies
    word_counts = Counter()
    total_size = 0 # Capture total file size

    # Open the input file and get its total size for progress tracking
    with open(text_file, 'r', encoding='utf-8') as f_in:
        f_in.seek(0, 2)  # Move to the end of the file
        total_size = f_in.tell()  # Get the total size of the file
        f_in.seek(0)  # Return to the beginning of the file

        processed_size = 0  # Track how much of the file has been processed
        while True:
            # Read the file in chunks and convert the text to lowercase
            chunk = f_in.read(chunk_size).lower()
            if not chunk:
                break  # Exit loop if no more content to read

            # Find all alphabetic words in the chunk
            words = re.findall(r'\b[a-z]+\b', chunk)
            # Update the word count with the words found in this chunk
            word_counts.update(words)

            # Calculate and display the progress percentage
            processed_size += len(chunk)
            progress_percentage = (processed_size / total_size) * 100
            print(f"Processing: {progress_percentage:.2f}% complete", end='\r')

    print("\nProcessing complete!")

    # Extract the 30 most common words
    top_30_words = word_counts.most_common(30)

    # Write the 30 most common words to the output CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Word', 'Count'])  # Write the header row
        csvwriter.writerows(top_30_words)  # Write the word counts

    # Confirmation message when the process is done
    print(f"30 most common words have been extracted to {output_csv}")

if __name__ == "__main__":
    text_file = 'q1_task1_alltext.txt'  # Path to the input text file
    output_csv = 'top_30_words.csv'  # Path to the output CSV file
    process_file(text_file, output_csv)
