import csv 
from newsstream_rss import feed_fetched 
from textcleaner import cleantexts, cleantext
from pos_tagger import pos_list
from syntax import syntax_score, syntax_list
from db_tools import remove_duplicates, clean_db, cleaned_strings
import spacy 
nlp = spacy.load('en_core_web_sm')
demos = ["Indian court refuses to lift deadline for Kotak Mahindra stake dilution", "Kotak Mahindra Bank surges on report of likely Berkshire investment", "Kotak Mahindra Bank jumps on report of Berkshire investment", "Kotak Mahindra Bank challenges RBI decision on preference shares", "High Court refuses to stay deadline for Kotak Mahindra Bank stake dilution: CNBC TV18", "Nifty, Stabe ensex rise; Kotak Mahindra Bank sees best day in nearly 9 years", "Indian shares rise; Kotak Mahindra Bank sees best day in nearly 9 yrs","Indian shares rise; Kotak Mahindra Bank sees best day in nearly 9 yrs" ]

def avg_risk(corp):
    scores = syntax_score(corp)
    riskavg = sum(scores)/len(scores)
    return int(riskavg)

def extract_phrases(corps):
    keys_ = []
    for sent in corps:
        docs = nlp(sent).noun_chunks
        text = [f.text for f in docs]
        keys_.append(text)
    keys = list(set([item for sublist in keys_ for item in sublist]))
    return keys

def risk_factors(corp):
    scores = syntax_score(corp)
    scored = zip(corp, scores)
    risk = []
    for scrd in scored:
        if scrd[1] > 0: 
            risk.append(scrd)
    return risk

def risk_mitigators(corp):
    scores = syntax_score(corp)
    scored = zip(corp, scores)
    risk = []
    for scrd in scored:
        if scrd[1] < 0: 
            risk.append(scrd)
    return risk

def main_ews(docs):
    cdocs = cleantexts(docs)
    phrases = extract_phrases(cdocs)
    risk = risk_factors(cdocs)
    risk_m = risk_mitigators(cdocs)
    avg = avg_risk(cdocs)
    return [avg, risk, risk_m, phrases]
