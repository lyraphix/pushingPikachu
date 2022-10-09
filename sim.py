import numpy as np
from numpy import dot
from numpy.linalg import norm

def sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def simWords(a, b):
    return sim(numpy.array((list)(map(float, wordDict[a]))), numpy.array((list)(map(float, wordDict[b]))))
