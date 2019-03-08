from textcleaner import stopwords
import csv
from textcleaner import cleantext
def remove_duplicates(filepath):
    rows = csv.reader(open(filepath, 'rt'))
    new = []

    for row in rows:
        if row not in new:
            new.append(row)

    writer = csv.writer(open(filepath, 'wt'))
    writer.writerows(new)

def clean_db(path):
    csv_reader = csv.reader(open(path, mode='rt'), delimiter=',')
    n = []
    for row in csv_reader:
        if row[0] not in stopwords:
            n.append(row)
    csv.writer(open(path, 'wt')).writerows(n)

def cleaned_string(sent):
    sent_ = cleantext(sent)
    s_ls = ' '.join(list(set(sent_.split(" "))))
    return s_ls

def cleaned_strings(sents):
    k = [(cleaned_string(sent)) for sent in sents]
    return k 

def lowercase(sent):
    sentL = sent.lower()
    return sentL

def lowercaser(sents):
    lower = [lowercase(sent) for sent in sents]
    return lower

def setName(name,corp):
    
    return 

def setNames(ls, lsa):
    
    return 


