import os
import warnings
import csv
import spacy
from collections import Counter

# Ignore specific warnings
warnings.filterwarnings('ignore', message='possible set union')
warnings.filterwarnings("ignore", category=FutureWarning)

# Load SpaCy model for diseases and drugs recognition
bc5cdr_nlp = spacy.load("en_ner_bc5cdr_md")

# File paths
input_file = "q1_task1_alltext_nonnumeric.txt"
output_csv = "q1_task4_spacy_entity_comparison.csv"

# Function to load the large text file in chunks
def load_large_text_file_in_chunks(file_path, chunk_size=500):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Extract entities using SpaCy
def extract_entities_spacy(chunk):
    doc = bc5cdr_nlp(chunk)
    diseases_spacy = [ent.text for ent in doc.ents if ent.label_ == "DISEASE"]
    drugs_spacy = [ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"]
    return diseases_spacy, drugs_spacy

# Process the large file and track unique entities
def process_large_file_spacy(input_file, chunk_size=500):
    all_diseases_spacy = set()
    all_drugs_spacy = set()

    file_size = os.path.getsize(input_file)
    processed_size = 0

    for chunk in load_large_text_file_in_chunks(input_file, chunk_size):
        diseases_spacy, drugs_spacy = extract_entities_spacy(chunk)

        # Update unique entity sets
        all_diseases_spacy.update(diseases_spacy)
        all_drugs_spacy.update(drugs_spacy)

        # Update processed size and calculate percentage
        processed_size += len(chunk.encode('utf-8'))
        progress = (processed_size / file_size) * 100
        print(f"Processing SpaCy: {progress:.2f}% complete", end="\r")

    return all_diseases_spacy, all_drugs_spacy

# Get top 50 most common words and their frequencies
def get_top_entities(entities):
    entity_counter = Counter(entities)
    return entity_counter.most_common(50)

# Write the comparison results to a CSV file
def write_comparison_to_csv(output_csv, top_spacy_entities):
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Spacy Entities', 'Frequency'])

        for entity, frequency in top_spacy_entities:
            writer.writerow([entity, frequency])

# Main execution for SpaCy
def main_spacy():
    print("Processing file with SpaCy and extracting entities...")

    all_diseases_spacy, all_drugs_spacy = process_large_file_spacy(input_file)

    all_spacy_entities = list(all_diseases_spacy) + list(all_drugs_spacy)

    print(f"\nTotal unique SpaCy entities (Diseases & Drugs): {len(all_spacy_entities)}")

    top_spacy_entities = get_top_entities(all_spacy_entities)

    write_comparison_to_csv(output_csv, top_spacy_entities)

    print(f"\nProcessing SpaCy complete. Results saved to {output_csv}")

# Run the SpaCy program
main_spacy()
