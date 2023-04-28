import pandas as pd

url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df=pd.read_csv(url,sep="\t")
pd.set_option('display.width', 1000)

# df= df.head(10)
# df=df.shape
# shape ile (row,column) sayısı görülebilir

# x=len(df.columns)
# kolon sayısı
# y=df.columns
# for i in y:
#     print(i)

# df= df.index
# RangeIndex(start=0, stop=4622, step=1) bilgilerine ulaşılır.

# df=df.groupby("item_name").sum().sort_values("quantity",ascending=False).head(1)
# en çok sipariş edilen ürüne ulaşıldı.

# df=df.groupby("choice_description").sum().sort_values("quantity",ascending=False).head(1)
# choice_description kolonundaki en çok sipariş edilen ürün

# df=df["quantity"].sum()
# toplam sipariş

# floatize = lambda x:float(x[1:-1])
# df["item_price"] = df["item_price"].apply(floatize)
# item_price kolonundaki $ ve sondaki boşluklardan kurtulundu. Float türüne dönüştürüldü.

# salary= (df["quantity"] * df["item_price"]).sum()
# print(salary)
# toplam kazanç

# totalorder = df["order_id"].value_counts().sum()
# print(totalorder)7
# toplam sipariş

# salary= (df["quantity"] * df["item_price"])
# df["revenue"] = salary
# revenue kolonu oluşturuldu ve her üründen ne kadar kazanıldığı eklendi.

# df= df["item_name"].value_counts()
# her bir üründen kaçar tane satıldığı bulundu.
# df = df.count()
# kaç farklı ürün satıldığı bulundu


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(df)