import pandas as pd

def csv_to_txt(csv):
    df = pd.read_csv(csv)
    itemlist = list(df['content'])


    with open("outfile", "w", encoding='utf-8') as outfile:
        outfile.write("\n".join(itemlist))
