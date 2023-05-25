import pandas as pd
import json
from kafka import KafkaProducer
import time
# # CSV dosyasını okuyun
augmented_data = pd.read_csv("iot_telemetry_data.csv")


# Verileri JSON formatına dönüştürün ve sırayla gönderin
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for _, row in augmented_data.iterrows():
    time.sleep(1)
    data_dict = row.to_dict()
    json_data = json.dumps(data_dict)
    producer.send('ornek', json_data.encode('utf-8'))

producer.flush()
producer.close()