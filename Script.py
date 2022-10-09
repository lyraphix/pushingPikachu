

import pandas as pd
import json
import re

def clean(csv, csv_out):
    tweetfile = open(csv,'rb')
    tweet = tweetfile.read()

    x = pd.read_json(tweet, lines=True)
    header = ['content']
    data = pd.DataFrame(x['content'], columns = header)
    i = 0
    for line in data['content']:

        line = line.lower()
        line = re.sub("@[A-Za-z0-9_]+","", line)
        line = re.sub("#[A-Za-z0-9_]+","", line)
        line = re.sub(r"http\S+", "", line)
        line = re.sub(r"www.\S+", "", line)
        line = re.sub(r"t.co\S+", "", line)
        line = re.sub("@[\&lt;]", "<", line)

        data['content'][i] = line
        i += 1

    data.to_csv(csv_out, sep=',', index=False, encoding='utf-32')
