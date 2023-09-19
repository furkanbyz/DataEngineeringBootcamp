#gerekli kutuphaneleri ice aktar
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
import json
from kafka import KafkaProducer
import time


#Yahoo Finance'dan finansal verileri cek
yf.pdr_override()

# tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
tech_list = ["AAPL", "MSFT", "IBM", "GOOG", "ORCL"]

#baslangic ve bitis tarihini belirt
end = datetime.now()
start = datetime(end.year - 10, end.month, end.day)

#her bir veriyi bir degisken olarak ata 
for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)
    


#Her bir sirketin verilerini iceren bir liste olustur
# company_list = [AAPL, GOOG, MSFT, AMZN]
company_list = [AAPL, MSFT, IBM, GOOG, ORCL]
# company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
company_name = ["APPLE", "MICROSOFT", "IBM", "GOOGLE", "ORACLE"]

#dataframe'e company_name adinda yeni bir kolon ekle
for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name

#verileri satir bazinda birlestir    
df = pd.concat(company_list, axis=0)
df.reset_index(inplace=True)

#tarihi formatla
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Float formatini duzenle
pd.options.display.float_format = '{:.2f}'.format

# CSV dosyasina kaydet
csv_filename = "stocks.csv"
df.to_csv(csv_filename, index=False)