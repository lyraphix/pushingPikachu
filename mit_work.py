# Code source: https://towardsdatascience.com/fine-tune-glove-embeddings-using-mittens-89b5f3fe4c39

import csv
import numpy as np
import mittens
import nltk
from mittens import Mittens
from collections import Counter
from nltk.corpus import brown
from mittens import GloVe
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def glove2dict(glove_filename):
    with open(glove_filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=' ',quoting=csv.QUOTE_NONE)
        embed = {line[0]: np.array(list(map(float, line[1:])))
                for line in reader}
    return embed

glove_path = "glovedata\glove.twitter.27B.100d.txt"
pre_glove = glove2dict(glove_path)

sw = set(nltk.corpus.stopwords.words('english'))
brown_data = nltk.corpus.brown.words()[:200000]
brown_nonstop = [token.lower() for token in brown_data if (token.lower() not in sw)]
oov = [token for token in brown_nonstop if token not in pre_glove.keys()]

def get_rareoov(xdict, val):
    return [k for (k,v) in Counter(xdict).items() if v<=val]

#oov_rare = get_rareoov(oov, 1)
#corp_vocab = list(set(oov) - set(oov_rare))
#brown_tokens = [token for token in brown_nonstop if token not in oov_rare]
#brown_doc = [' '.join(brown_tokens)]
oov_rare = get_rareoov(oov, 1)
corp_vocab = list(set(oov) - set(oov_rare))

corp_vocab = list(set(oov))
brown_doc = [' '.join(brown_nonstop)]

cv = CountVectorizer(ngram_range=(1,1), vocabulary=corp_vocab)
X = cv.fit_transform(brown_doc)
Xc = (X.T * X)
Xc.setdiag(0)
coocc_ar = Xc.toarray()

mittens_model = Mittens(n=100, max_iter=1)

new_embeddings = mittens_model.fit(coocc_ar, vocab=corp_vocab, initial_embedding_dict= pre_glove)

newglove = dict(zip(corp_vocab, new_embeddings))
f = open("repo_glove_100.pkl","wb")
pickle.dump(newglove, f)
f.close()
