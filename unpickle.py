import pickle
import numpy as np

df_file = open("glovedata/glove.twitter.27B.100d.txt", 'r', encoding='utf-8')
data = [vector.strip().split(" ") for vector in df_file.readlines()]
df_file.close()

wordDict = {}
for item in data:
    wordDict[item[0]] = item[1:]

for item in wordDict:
    for val in wordDict[item]:
        val = float(val)

f =  open("wordDict.pkl", 'wb')
pickle.dump(wordDict, f)
f.close()

"""sentenceArray = ['righthander', 'turnpikes', '']

sumArray = []

for word in sentenceArray:
    sumArray.append(data[word])

arr = np.array(sumArray)

result = np.average(arr,axis=0)


print(result)
"""
