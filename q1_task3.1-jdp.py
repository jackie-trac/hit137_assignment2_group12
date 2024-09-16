# An alternative answer to Question 1, Task 3.1 by Jerichoo

from collections import Counter
import re
import csv

def count_words(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Use regular expression to find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)
    
    return top_30_words

def save_to_csv(word_counts, csv_path):
    # Write the word counts to a CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(word_counts)

# Example usage
file_path = r'C:\Users\delpu_h93swxp\OneDrive\Desktop\HIT137Github\hit137_assignment2_group12\question1_task1_alltext.txt'  # Replace with your file path
csv_path = 'top_30_words.csv'  # Output CSV file path

top_30_words = count_words(file_path)
save_to_csv(top_30_words, csv_path)

print(f"Top 30 most common words have been saved to {csv_path}")
