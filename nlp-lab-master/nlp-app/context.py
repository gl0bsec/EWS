from textcleaner import cleantext, cleantexts
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from syntax import syntax_list, syntax_score, syntax_s
import pandas as pd
from collections import Counter
from db_tools import lowercaser
import numpy as np

def bn_probs(co_df, vocab, sents):
    prob_mat = []
    sentlist = [sent.split(" ") for sent in sents]
    vocab_flat = [item for sublist in sentlist for item in sublist]
    
    count = Counter(vocab_flat)

    sorted_count = dict(sorted(count.items()))
    
    freqs = list(sorted_count.values())
    for i, key in enumerate(vocab):
        row = co_df[key].tolist()
        probs = [e/freqs[i] for e in row] 
        prob_mat.append(probs)
    
    temp = np.array(prob_mat)
    temp = np.where(temp > 1.0, 1.0, temp)

    prob_df = pd.DataFrame(columns = vocab, index = vocab, data = temp)

    return prob_df

def return_cooc(docs):
    vec = CountVectorizer(ngram_range=(1,1))
    X = vec.fit_transform(docs)
    Xc = (X.T * X)
    Xc.setdiag(0)
    ccr = Xc.todense().tolist()
    vocab_d = vec.vocabulary_
    vocab = list(sorted(vocab_d.keys()))
    co_df = pd.DataFrame(columns = vocab, index = vocab, data = ccr)
    return co_df

def vocabulary(docs):
    vec = CountVectorizer(ngram_range=(1,1))
    X = vec.fit_transform(docs)
    vocab_d = vec.vocabulary_
    vocab = list(sorted(vocab_d.keys()))
    return vocab

def rescore(docs, prob_df, word):
    h_words = []
    ig = []

    vocab_ = vocabulary(docs)
    n_ =  vocab_.index(word)

    indexes = context(n_, prob_df.values.tolist())
    
    for indx in indexes: 
        h_words.append(vocab_[indx])
    scores = syntax_list(" ".join(h_words))
    
    if len(scores) == 0:
        return 0

    return sum(scores)/len(scores)

def context(n, prob_list):
    indexes = []
    ignr = []

    def maxiter(n, ignr_list, probm):
        wprob = probm[n]
        if len(ignr_list) != 0:
            ignore(n, ignr_list, probm)
        if max(wprob) == 0:
            return indexes
        if max(wprob) > 0:
            maxelem = max(wprob)
            indx = probm[n].index(maxelem)
            indexes.append(indx)
            ignr_list.append(n)
            maxiter(indx, ignr_list, probm)
            
            return indexes

    return maxiter(n, ignr, prob_list)

def context_sentence(sentence):
    syn_sc = sum(syntax_list(sentence))

    cleaned = cleaner([sentence])
    probm = bn_probs(return_cooc(cleaned), vocabulary(cleaned), cleaned)
    
    split = cleaned[0].split(' ')
    score = []

    for word in split:
        score.append(rescore(cleaned, probm, word))

    if syn_sc == 0:
        return sum(score)

    return (np.sign(syn_sc) * sum(score) / syn_sc) + syn_sc

def context_docs(docs):
    score = []
    
    for sent in docs:
        score.append(context_sentence(sent))

    return sum(score)/len(score)

def cleaner(docs):
    return lowercaser(cleantexts(docs))

def ignore(n, ignr_list, probm):
    wprob = probm[n]
    for val in ignr_list:
        wprob[val] = 0
