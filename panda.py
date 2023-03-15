import pandas as pd

veri = [["Yusuf","Zeki"],["Hakan","Özhan"],["Ömer","Özdemir"]]
# df = pd.DataFrame(veri)
# df = pd.DataFrame(veri,columns=["Ad","Soyad"])
# df = pd.DataFrame(veri,columns=["Ad","Soyad"], index=["index1","index2","index3"])

veri2={
    "ad":["Yusuf","Hakan","Ömer","Merve","Ali","Akın","Furkan","Nurşin"],
    "soyad":["Zeki","Çelik","Ak","Deli","Ağa","Sancar","Beyaz","Magın"],
    "yaş":[10,16,25,35,45,55,65,75]
}
df2=pd.DataFrame(veri2)
# df2.pop("yaş") 
# yaş kolonu silindi

print(df2.head)
print(df2.tail)
# print(df2["yaş"])
# print(df2)