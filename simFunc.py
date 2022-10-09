import numpy as np
from numpy import dot
from numpy.linalg import norm

def sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def simWords(a, b):
    a1 = map(float, wordDict[a]))
    b1 = map(float, wordDict[b]))
    a2 = numpy.array((list)a1)
    b2 = numpy.array((list)b1)
    return sim(a2, b2)
