import pandas as pd

df = pd.read_csv("data/fifa_cleaned.csv")

# df = df.head(10)

# LOC KULLANIMLARI

# df = df.loc[:,:]
# ["satır","sütun"] şeklinde düşünülebilir
# tüm satır ve sütunları gösterir

# df = df.loc[:10 ,"name"]
# name kolonunun 11.satırına kadar olan kayıtları gösterir.

# df = df.loc[6:15, "club_team"]
# club_team kolonunun 6-15 arası satırları dahil olacak şekilde gösterir

# df = df.loc[df["nationality"] == "Germany"]
# nationaly kolonu Germany olan kayıtlar gösterilir
# df = df[df["nationality"]=="Germany"]
# loc kullanılmadan bu şekilde de aynı veriler elde edilebilir
 
# df = df.loc[df["nationality"] == "Germany"][["name","value_euro"]].sort_values("value_euro",ascending=False)
# aynı kayıtlar üzerinde sıralama yapıldı






print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
# df = df.columns
print(df)
