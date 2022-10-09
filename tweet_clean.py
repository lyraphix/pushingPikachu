# snscrape --jsonl twitter-tweet 1524852430407553026 >tweet.txt
import pandas as pd
import json

def clean(tweet_txt, csv_name):
    jsonList = []
    with open(tweet_txt, 'rb') as f:
        for jsonObj in f:
            dict = json.loads(jsonObj)
            jsonList.append(dict)
    dfItem = pd.DataFrame.from_records(jsonList)
    dfItem = pd.DataFrame(dfItem['content'], columns = ['content'])

    dfItem.to_csv(csv_name, sep=',', index=False, encoding='utf-32')
