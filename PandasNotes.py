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

# df1 = pd.read_csv("Data/ufo.csv")
# df2 = pd.read_csv("Data/grades.csv")

df1 = pd.DataFrame({'person': ['Cem', 'Can'], 'department': [
                   'Engineering', 'Marketing']})
df2 = pd.DataFrame({'person': ['Can', 'Cem'], 'date': [2017, 2018]})

# df3 = pd.concat([df1,df2])
# df1 ve df2yi birleştirdi, diğerinde bulunmayan kolonlar için nan değeri girilir

# df3 = pd.concat([df1, df2], ignore_index=True)
# df1 ve df2yi birleştirip index sırasını düzeltti, diğerinde bulunmayan kolonlar için nan değeri girilir

# df3 = pd.concat([df1, df2], axis=1)
# df1 ve df2yi yan yana ekledi (satır olarak), nan olarak bırakmayıp index bilgilerini düzenledi. iki adet person kolonu var !!!
# https://towardsdatascience.com/pandas-concat-tricks-you-should-know-to-speed-up-your-data-analysis-cd3d4fdfe6dd detay için incelenebilir

# df3 = pd.merge(df1, df2)
df3 = pd.merge(df1, df2, on="person")
#Hangi kolonu baz alarak  işlem yapacağımızı seçebiliriz

# MERGE CONCAT FARKI
# Consider you have a dataset than contains credit card transactions. You have a bunch of columns about the details of a transaction and one column indicating customer ID. Another dataframe includes more detailed information about a customer and the customer ID as well. In order to combine these two dataframes, we can merge them on “customer ID” column so that entries match.

df4 = pd.DataFrame({'department': ['Engineering', 'Marketing'],'head': ['Mete', 'Taylan']})

df5 = pd.merge(df3,df4)

print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df1:")
print(df1)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df2:")
print(df2)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df3:")
print(df3)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df4:")
print(df4)
print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print("df5:")
print(df5)




# print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
# df = df.columns
# print(df)
