import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')

# df = df.sort_values("beer_servings", ascending=False).head(30)

# df = df.groupby("continent")["beer_servings"].mean()
# Which continent drinks more beer on average?

# df = df.groupby("continent")["wine_servings"].describe()
# her kıta için wine_servings istatistikleri

# df  = df.groupby("continent").mean()
# kıtalara göre groupby yapıldı

# df = df.groupby("continent").median()
# kıtalara göre groupby yapıldı, medyanı alındı.

# df = df.groupby("continent")["spirit_servings"].agg(["mean","min","max"])
# kıtalara göre groupby yapıldı, spirit_servings kolonunun yukarıdaki değerleri alındı



print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print(df)
