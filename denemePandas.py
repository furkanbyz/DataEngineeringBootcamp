import pandas as pd
import numpy as np

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

# df = df.loc[ (df["nationality"] == "Germany") & (df["value_euro"] > 38000000) ].head()
# df = df[ (df["nationality"] == "Germany") & (df["value_euro"] > 38000000)].head()
# ikisi de aynı sonucu verir


# ILOC KULLANIMI

# df = df.iloc[:,:]
# tüm kayıtları verir

# df = df.iloc[:6 , 1:6]
# 0-6 arası satırlar, 1-6 arası sütunlar


# EKSİK VERİ (NaN, Null...) (fillna(), dropna(),)

# df = df.isna()
# null değer varsa True döner

# df = df.fillna(False)
# null değerleri False ile doldurur

# df = df.fillna(df.mean())
# null değerleri ortalama ile doldurur

# df = df.fillna(df.mean()["Column1"])
# Column1 deki null değerleri ortalama ile doldurur

# df = df.dropna()
# satırda ya da sütunda null değer varsa o satırı siler

# df = df.isna()
# df = df.dropna()
# df = df.isna()
# null değerlerin olduğu satırların silindiği bu şekilde görülebilir

# df = df.dropna(axis="columns")
# kolona göre siler


# SIRALAMA (sort_values())

# df = df.sort_values(by="value_euro", ascending= False)
# büyükten küçüğe sıralar

# df = df.sort_index( ascending=False)
# indexe göre sıralar


# DATAFRAME BİRLEŞTİRME (concat(), merge())

df1 = pd.read_csv("Data/ufo.csv")
df2 = pd.read_csv("Data/grades.csv")

# df3 = pd.concat([df1,df2])
# df1 ve df2yi birleştirdi

# df3 = pd.concat([df1, df2], ignore_index=True)
# df1 ve df2yi birleştirip index sırasını düzeltti

df3 = pd.concat([df1, df2], axis=1)
# df1 ve df2yi yan yana ekledi (satır olarak)
# https://towardsdatascience.com/pandas-concat-tricks-you-should-know-to-speed-up-your-data-analysis-cd3d4fdfe6dd detay için incelenebilir


print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df1:",df1)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df2:",df2)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df3:",df3)


# https://cemayan.medium.com/pandas-ile-veri-analizi-2-data-selection-missing-values-4ecec921be87  son olarak merge kaldı
# https://cemayan.medium.com/pandas-ile-veri-analizi-3-aggregation-and-grouping-f74ce504bc30  devamı



# print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
# df = df.columns
# print(df)
