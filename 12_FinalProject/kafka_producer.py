#gerekli kutuphaneleri ice aktar
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
import json
from kafka import KafkaProducer
import time

# Yahoo Finance'dan finansal verileri çek
yf.pdr_override()

tech_list = ['AAPL', 'MSFT', 'IBM', 'GOOG', 'ORCL']

# Başlangıç ve bitiş tarihini belirt
end = datetime.now()
start = datetime(end.year - 10, end.month, end.day)

# Her bir veriyi bir değişken olarak ata 
for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)

# Her bir şirketin verilerini içeren bir liste oluştur
company_list = [AAPL, MSFT, IBM, GOOG, ORCL]
company_name = ["APPLE", "MICROSOFT", "IBM", "GOOGLE", "ORACLE"]

# DataFrame'e company_name adında yeni bir kolon ekle
for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name

# Verileri satır bazında birleştir    
df = pd.concat(company_list, axis=0)
df.reset_index(inplace=True)

# Tarihi formatla
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Float formatını düzenle
pd.options.display.float_format = '{:.2f}'.format

# DataFrame kolon isimlerini değiştir
df = df.rename(columns={
    "company_name": "firma",
    "Open": "acilis",
    "High": "en_yuksek",
    "Low": "en_dusuk",
    "Close": "kapanis",
    "Adj Close": "hacim",
    "Date": "tarih"
})

# CSV dosyasına kaydet
csv_filename = "tech_stocks.csv"
df.to_csv(csv_filename, index=False)

# Kafka yolunu ve topic adını belirt
server = "localhost:9092"
topic_name = "stocks2" # değiştirilebilir

# Verileri JSON formatına dönüştür
producer = KafkaProducer(
    bootstrap_servers=server,
    value_serializer=lambda x: json.dumps(x).encode("UTF-8")
)

# JSON formatına dönüştürülen her bir veriyi Kafka'ya gönder
for _, row in df.iterrows():
    to_json = row.to_dict()
    time.sleep(1)
    producer.send(f'{topic_name}', value=to_json)
    producer.flush()

producer.close()
