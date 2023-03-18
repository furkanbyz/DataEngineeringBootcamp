import pandas as pd

data = pd.read_csv("../data/youtube-ing.csv")

# data = data.head(20)
# data = data[10:15]
# data = data.columns
# data = data.shape[0]

# data = data.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],  axis=1)
# kolon silme

# data = data[["likes","dislikes"]].mean()
# likes dislikes ortalama

# data = data[["title","likes","dislikes"]].head(50)

# data = data[["title","views"]].sort_values(by="views",ascending=False)
# izlenme sayısına göre sıralama

# data = data[data["views"].max() == data["views"]][["title","views"]]
# data = data[data["views"].max() == data["views"]]["title"].iloc[0]
# en çok izlenen kaydı getirdi

# data = data[data["views"].min() == data["views"]][["title","views"]]
# en az izlenen kaydın satırını getirdi
# data = data[data["views"].min() == data["views"]]["views"].iloc[0]
# en az izlenen kaydın izlenme sayısını getirdi

# data = data.sort_values(by="views",ascending=False)[["title","views"]].head(10)
# en çok izlenme sayısı olan ilk 10 kayıt

# data = data.groupby("category_id").mean().sort_values("likes",ascending=False)["likes"]
# kategoriye göre beğeni ortalamaları sıralandı

# data = data.groupby("category_id").sum().sort_values(by="comment_count",ascending=False)["comment_count"]
# kategoriye göre yorum sayıları sıralandı

# data = data["category_id"].value_counts()
# her kategoride kaç kayıt var

# data["titleLen"] = data["title"].apply(len)
# title uzunluklarını gösteren yeni bir kolon oluşturuldu

# ratio = data["likes"]/data["dislikes"]
# data["popularity"] = ratio
# data = data.dropna()
# data = data.sort_values("popularity",ascending=False)[["title","likes","dislikes","popularity"]].head(20)
# like dislike oranına göre popülarite kolonu oluşturuldu ve sıralama yapıldı

# data["tagCount"] = data["tags"].apply(lambda x: len(x.split('|')))
# data= data.loc[:, "description":]
# tag count kolonu ile tags kolonunda kaç tane etiket olduğu sayılıp kolonda gösterildi




print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print(data)
