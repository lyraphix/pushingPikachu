import numpy as np
from numpy import dot
from numpy.linalg import norm

def sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def simWords(a, b):
    a1 = (list)(map(float, wordDict[a]))
    b1 = (list)(map(float, wordDict[b]))
    a2 = numpy.array(a1)
    b2 = numpy.array(b1)
    return sim(a2, b2)
