import context
from context import probmat_, vocabulary, demos, probmat
from EWS import demo2
import numpy as np

indexes = []
ls = probmat_.tolist()

def maxiter(n, ignr_list, probm):
    wprob = probm[n]

    if len(ignr_list) != 0:
        ignore(n, ignr_list, probm)

    if max(wprob) == 0:
        return indexes 

    if max(wprob) > 0:
        maxelem = max(wprob)
        #print(maxelem)

        indx = probm[n].index(maxelem)
        indexes.append(indx)

        ignr_list.append(n)
        maxiter(indx, ignr_list, probm)

        return indexes

def ignore(n, ignr_list, probm):
    wprob = probm[n]
    for val in ignr_list:
        wprob[val] = 0

g = 2
ig = []
#print(probmat.to_string())
maxiter(g, ig, ls)
print(indexes)
