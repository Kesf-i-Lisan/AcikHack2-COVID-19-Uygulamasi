from summarizer import Summarizer
import pandas as pd

df = pd.read_csv("./dataframe.csv",encoding="utf-8-sig")

model = Summarizer()

ozet_list = []
for i in df['Metin']:
    result = model(i, min_length=60)
    full = ''.join(result)
    ozet_list.append(full)

df["BERT_Ozet"] = ozet_list
df.to_csv("dataframe_ozet_v2.csv",encoding="utf-8-sig")