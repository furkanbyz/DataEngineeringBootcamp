import pandas as pd

url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df=pd.read_csv(url,sep="\t")
pd.set_option('display.width', 1000)

print(df.tail())