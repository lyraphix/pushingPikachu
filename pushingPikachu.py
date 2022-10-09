import numpy as np
from numpy import dot
from numpy.linalg import norm
import random

# file = np.load("repo_glove_100.pkl", allow_pickle = 'true')

wordDict = np.load("wordDict.pkl", allow_pickle = 'true')
entry_list = list(wordDict.items())

def sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def simWords(a, b):
    a1 = (list)(map(float, wordDict[a]))
    b1 = (list)(map(float, wordDict[b]))
    a2 = np.array(a1)
    b2 = np.array(b1)
    return sim(a2, b2)

def findSynonym(word, tries=100000, p=False):
    i = 0
    val = 0
    result = ""
    while i < tries:
        b = random.choice(entry_list)
        if simWords(b[0], word) > val:
            val = simWords(b[0], word)
            result = b[0]
        i += 1
        if(p):
            if i%100==0:
                print(result)
    print(result)
