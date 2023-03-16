import pandas as pd

team={
    "Name":["Enner","Michy","Emre","Miha","Arda","Atilla","Luan"],
    "Surname":["Valencia","Batshuayi","Mor","Zajc","Güler","Szalai","Peres"],
    "Position":["Forward","Forward","Midfield","Midfield","Midfield","Defence","Defence"],
    "Shirt Number":[9,11,15,10,17,3,2],
    "Goals":[23,11,4,5,5,2,1]
}

df= pd.DataFrame(team)

print(df)