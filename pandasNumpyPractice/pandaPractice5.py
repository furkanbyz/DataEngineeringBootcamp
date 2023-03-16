import pandas as pd
import numpy as np

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)

# df= df.loc[:,"school":"guardian"]
# ilgili satır ve sütun aralıkları alındı

capitilaze = lambda x: x.capitalize()
# baş harf bütüyen bir lambda fonksiyonu oluşturuldu

df["Mjob"] = df["Mjob"].apply(capitilaze)
df["Fjob"] = df["Fjob"].apply(capitilaze)
# lambda fonksiyonu burada çağrıldı

# df = df.tail(1)
# son element alındı

# def majority(x):
#     if x>17:
#         return True
#     else: False
# df["legal_drinker"] = df["age"].apply(majority)
# majortiy fonk oluşturuldu ve legal.. sütunu oluşturulup age sütunu üzerinde kullanıldı

print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print(df)