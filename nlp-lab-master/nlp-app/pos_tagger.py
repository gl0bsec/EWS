import spacy
import csv
import sys

# Load english language
nlp = spacy.load('en_core_web_sm')

# For pretty printing of tokenisation
def print_table(doc):
    header = '| {:10} | {:10} | {:10} |'.format("Text", "PoS", "Tag")
    separator = '-' * len(header)

    print(header)
    print(separator)
    
    for token in doc:
        print('| {:10} | {:10} | {:10} |'.format(token.text, token.pos_, token.tag_))

# Write tagged.csv to the current directory
def write_csv(doc):
    with open('tagged.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        for token in doc:
            writer.writerow([token.text, token.pos_, token.tag_])

# pos tagging for lists
def pos_list(sentences):
    for sentence in sentences:
        doc = nlp(u'{}'.format(sentence))
        write_csv(doc)

# pos tagging for csv with relative filepath 
def pos_csv(filepath):
    with open(filepath, 'r', newline='') as text:
        reader = csv.reader(text, delimiter=';', quotechar='|')
        for sentence in reader:
            doc = nlp(u'{}'.format(sentence))
            write_csv(doc)

