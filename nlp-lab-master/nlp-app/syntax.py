import csv
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def syntax_s(text):
    db = csv.reader(open(os.path.join(__location__, 'scored.csv'), mode='rt'), delimiter=',')
    for row in db:
        if text == row[0]:
            return int(row[3])
    return 0

def syntax_list(sentence):
    score = []
    for word in sentence.split(" "):
        score.append(syntax_s(word))
    cleaned = list(filter(lambda x: x != 0, score))
    return cleaned

def syntax_score(docs):
    scores = []
    for doc in docs:
        scores.append(sum(syntax_list(doc)))
    return scores
