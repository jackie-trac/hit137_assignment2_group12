'''
OUTPUT
This version will write down entities immediately as it goes. 
However, it doesn't count unique total entities and doesn't report top common words
'''
import os
import warnings
import csv
import torch
import transformers
import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Ignore specific warnings for cleaner output
warnings.filterwarnings('ignore', message='possible set union')
warnings.filterwarnings('ignore', message='clean_up_tokenization_spaces')

# Load BioBERT model and tokenizer
model_name = 'dmis-lab/biobert-base-cased-v1.1'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)

# Load SciSpacy models for diseases and drugs recognition
sci_sm_nlp = spacy.load("en_core_sci_sm")
bc5cdr_nlp = spacy.load("en_ner_bc5cdr_md")

# Set the directory of the input text file
input_file = "q1_task1_alltext_nonnumeric.txt"
output_file = "q1_task1_output_entities.csv"

# Function to load the large text file in chunks
def load_large_text_file_in_chunks(file_path, chunk_size=500):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Extract entities using SciSpacy
def extract_entities_spacy(chunk):
    doc = bc5cdr_nlp(chunk)
    diseases_spacy = [ent.text for ent in doc.ents if ent.label_ == "DISEASE"]
    drugs_spacy = [ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"]
    return diseases_spacy, drugs_spacy

# Extract entities using BioBERT
def extract_entities_biobert(chunk):
    ner_results = ner_pipeline(chunk)
    diseases_bert = [entity['word'] for entity in ner_results if "DISEASE" in entity['entity']]
    drugs_bert = [entity['word'] for entity in ner_results if "DRUG" in entity['entity']]
    return diseases_bert, drugs_bert

# Process the large file in chunks and append results to a CSV
def process_large_file_append_to_csv(input_file, output_csv, chunk_size=500):
    with open(output_csv, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['DISEASES_spacy', 'DRUGS_spacy', 'DISEASES_BERT', 'DRUGS_BERT'])

        # Process file in chunks
        for i, chunk in enumerate(load_large_text_file_in_chunks(input_file, chunk_size)):
            print(f"Processing chunk {i + 1}...")  # Progress notification

            # Extract entities with SpaCy and BioBERT
            diseases_spacy, drugs_spacy = extract_entities_spacy(chunk)
            diseases_bert, drugs_bert = extract_entities_biobert(chunk)

            # Write results to CSV
            for j in range(max(len(diseases_spacy), len(drugs_spacy), len(diseases_bert), len(drugs_bert))):
                writer.writerow([
                    diseases_spacy[j] if j < len(diseases_spacy) else "",
                    drugs_spacy[j] if j < len(drugs_spacy) else "",
                    diseases_bert[j] if j < len(diseases_bert) else "",
                    drugs_bert[j] if j < len(drugs_bert) else ""
                ])
    
    print(f"Processing complete. Results saved to {output_csv}")

# Call the processing function
process_large_file_append_to_csv(input_file, output_file, chunk_size=500)



