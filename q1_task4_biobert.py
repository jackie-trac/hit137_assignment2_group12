import os
import warnings
import csv
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import Counter

# Ignore specific warnings
warnings.filterwarnings('ignore', message='clean_up_tokenization_spaces')
warnings.filterwarnings("ignore", category=FutureWarning)

# Load BioBERT model and tokenizer
model_name = 'dmis-lab/biobert-base-cased-v1.1'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)

# File paths
input_file = "q1_task1_alltext_nonnumeric.txt"
output_csv = "q1_task4_biobert_entity_comparison.csv"

# Function to load the large text file in chunks
def load_large_text_file_in_chunks(file_path, chunk_size=500):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Extract entities using BioBERT
def extract_entities_biobert(chunk):
    ner_results = ner_pipeline(chunk)
    diseases_bert = [entity['word'] for entity in ner_results if "DISEASE" in entity['entity']]
    drugs_bert = [entity['word'] for entity in ner_results if "DRUG" in entity['entity']]
    return diseases_bert, drugs_bert

# Process the large file and track unique entities
def process_large_file_biobert(input_file, chunk_size=500):
    all_diseases_bert = set()
    all_drugs_bert = set()

    file_size = os.path.getsize(input_file)
    processed_size = 0

    for chunk in load_large_text_file_in_chunks(input_file, chunk_size):
        diseases_bert, drugs_bert = extract_entities_biobert(chunk)

        # Update unique entity sets
        all_diseases_bert.update(diseases_bert)
        all_drugs_bert.update(drugs_bert)

        # Update processed size and calculate percentage
        processed_size += len(chunk.encode('utf-8'))
        progress = (processed_size / file_size) * 100
        print(f"Processing BioBERT: {progress:.2f}% complete", end="\r")

    return all_diseases_bert, all_drugs_bert

# Get top 50 most common words and their frequencies
def get_top_entities(entities):
    entity_counter = Counter(entities)
    return entity_counter.most_common(50)

# Write the comparison results to a CSV file
def write_comparison_to_csv(output_csv, top_bert_entities):
    with open(output_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['BioBERT Entities', 'Frequency'])

        for entity, frequency in top_bert_entities:
            writer.writerow([entity, frequency])

# Main execution for BioBERT
def main_biobert():
    print("Processing file with BioBERT and extracting entities...")
    all_diseases_bert, all_drugs_bert = process_large_file_biobert(input_file)
    all_bert_entities = list(all_diseases_bert) + list(all_drugs_bert)
    print(f"\nTotal unique BioBERT entities (Diseases & Drugs): {len(all_bert_entities)}")
    top_bert_entities = get_top_entities(all_bert_entities)
    write_comparison_to_csv(output_csv, top_bert_entities)
    print(f"\nProcessing BioBERT complete. Results saved to {output_csv}")

# Run the BioBERT program
main_biobert()
