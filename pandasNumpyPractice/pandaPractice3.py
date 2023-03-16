import pandas as pd

data = pd.read_csv(
    'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv', sep=',')

# data = data[["Team","Goals"]]
# Team and Goals columns is displayed

# data = data["Team"].shape
# number = data[0]
# toplam takım sayısı alındı (satır sayısı)

# data= data.shape[1]
# sütun sayısı alındı

# data = data[["Team","Yellow Cards","Red Cards"]]
# istenilen sütunlar alındı

# data = data[["Team","Yellow Cards","Red Cards"]].sort_values(["Red Cards","Yellow Cards"],ascending=False)
# datadan sonra göstermek istedinilen sütunlar, sorttan sonra da hangilerinin sıralanacağı belirtlidi.

# data = data["Yellow Cards"].mean()
# ortalama alındı

# data = data[data["Goals"]>6]
# 6dan fazla gol atan takımlar

# data = data[data["Team"].str.startswith("G")]
# adı G ile başlayan takımlar alındı

# data = data[data["Team"].str.endswith("n")]
# adı n ile biten takımlar alındı

# data = data.iloc[3:6, 0:3]
# sadece 3:6 satır ve 0:3 sütunları alındı

# data = data.iloc[:, :-3]
# sondan 3 kolon hariç gösterildi


# data = data.loc[data.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]
# isin() fonk kullanılarak, team kolonunda england ıtaly russia alındı



print("@@@@@@@@@@@@@@@@@@@@ OUTPUT @@@@@@@@@@@@@@@@@@@@")
print(data)
