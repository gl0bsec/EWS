import spacy
import csv
import sys

# Load english language
nlp = spacy.load('en_core_web_sm')

# For pretty printing of tokenisation
def print_table(doc):
    header = '| {:10} | {:10} |'.format("Text", "Dependencies")
    separator = '-' * len(header)

    print(header)
    print(separator)
    
    for token in doc:
        print('| {:10} | {:10} |'.format(token.text, token.dep_))

# Write text.csv to the current directory
def write_text_csv(doc):
    with open('text.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        for token in doc:
            writer.writerow([token.text])

# Write deps.csv to the current directory
def write_csv(doc):
    with open('deps.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        for token in doc:
            writer.writerow([token.dep_])

# dep parsing for lists
def dep_list(sentences):
    for sentence in sentences:
        doc = nlp(u'{}'.format(sentence))
        write_csv(doc)
        write_text_csv(doc)

# dep parsing for csv with relative filepath 
def dep_csv(filepath):
    with open(filepath, 'r', newline='') as text:
        reader = csv.reader(text, delimiter=';', quotechar='|')
        for sentence in reader:
            doc = nlp(u'{}'.format(sentence))
            write_csv(doc)
            write_text_csv(doc)

