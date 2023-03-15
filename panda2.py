import pandas as pd

# df= pd.read_csv("data/grades.csv")
# df = df.head()
# df = df. tail(11)
# df.columns=["İSİM","SOYAD","ssn","test1","test2","test3","test4","FINAL","GRADE"]
# pd.set_option('display.width', 500)
# df = df.rename(columns={"İSİM":"İsim"})
# pd.set_option('display.max_columns', 500)

# print(df.loc[0:4])
# # loc 4. veriyi de alır
# print("----------------")
# print(df.iloc[0:4])
# # iloc 4. veriyi almaz
# print("----------------")
# print(df[0:4])
# print("----------------")
# print(df.iloc[:,1])
# print("----------------")
# print(df.iloc[6:14,1])
# print(df.iloc[6:14,"Grade"])
# print(df.iloc[0:4,0])
# 0dan 4e kadar alır sadece 0. sütunu yani name sütununu yazdırır.


# print(df.iloc[:6,1:5])
# print(df.iloc[:5,[1,8]])
# print(df.loc[:5,["First name","Final"]])
# print(df.loc[::-1,["Last name"]])
# print(df.columns)

# df = pd.read_csv("data/imdb_1000.csv")
# df=df[2:5][["star_rating","duration"]]
# df=df["star_rating"]>8.5
# true false olarak getirir
# df= df[df["star_rating"]>9.1]
# true false yerine değeri yazarak getirir.

# df= df.loc[df["star_rating"]>9.1]
# yukarıdaki işlemi loc ile yapılışı

# df= df[(df["star_rating"]>=8) & (df["star_rating"]<=9)]
# df= df.loc[(df["star_rating"]>=8) & (df["star_rating"]<=9)]["title"]
# df= df.loc[(df["star_rating"]>=8) & (df["star_rating"]<=9)][["title","star_rating"]]
# df= df.loc[(df["star_rating"]> 8) & (df["star_rating"]< 9) & (df["genre"]=="Drama"),["title","content_rating","genre","duration"]]

# GROUP BY
# df = df["star_rating"].max()
# df = df["star_rating"].sum()
# df = df["star_rating"].count()

# df = df.groupby("genre").star_rating.mean()
# df = df.groupby("genre")["star_rating"].mean()
# ikisi aynı sonucu verir

# df= df.groupby("genre")["star_rating"].agg(["count","mean","max","min"])

# DROP
# df= df.drop("content_rating",axis=1,inplace=True)
# ilgili sütun inplace true ile kalıcı olarak silinir

# df= df.drop(1,axis=0, inplace=True)
# satır silme


df = pd.read_csv("data/ufo.csv")
# df = df.notnull()
# df= df[df.notnull()]
# df= df[df.isnull()]
# df= df.notnull().sum()
# df= df.describe()

# df= df.dropna()
# null olanları siler

# df= df.dropna(subset=["City","State"])
# df= df["Shape Reported"].fillna(value="Belirsiz",inplace=True)
df = df["Shape Reported"].notnull()

print(df)

