import numpy as np
from numpy import dot
from numpy.linalg import norm

def sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def simWords(a, b):
    a1 = numpy.array((list)(map(float, wordDict[a])))
    b1 = numpy.array((list)(map(float, wordDict[b])))
    return sim(a1, b1)
