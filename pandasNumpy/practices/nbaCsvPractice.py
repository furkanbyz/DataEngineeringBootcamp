import pandas as pd

df = pd.read_csv("../data/nba.csv")

# df = df.head(10)

# df = df.shape[0]
# toplam kayıt sayısı

# df = df["Salary"].mean()
# salary ortalaması

# df = df["Salary"].max()
# df= df[df["Salary"] == df["Salary"].max()]
# maaşı en yüksek olan kaydı getirir ve ilgili sütunlarına buradan erişilebilir

# df = df[ (df["Age"] > 20) & (df["Age"] < 25) ][["Name", "Age"]].head(20)
# 20<yaş<25 koşulunu sağlanayanların isim yaş bilgileri

# df = df[(df["Name"]=="John Holland")]["Team"].iloc[0]
# ...

# df= df.groupby("Team").mean()["Salary"]
# takımların ortalama maaş bilgisi

# df=df["Team"].nunique()
# df = len(df.groupby("Team"))
# kaç farklı takım var, ikisi de aynı çıktıyı verir

# df = df["Team"].value_counts()
# hangi takımda kaç kayıt var

df=df.dropna(inplace=True)
# nan değerleri siler
# df = df[df["Name"].str.contains("and")]
# isminin içinde and olan kayıtlar gelir

# def strFind(name):
#     if "and" in name.lower():
#         return True
#     return False

# df = df[df["Name"].apply(strFind)]




print("@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@")
print(df)
