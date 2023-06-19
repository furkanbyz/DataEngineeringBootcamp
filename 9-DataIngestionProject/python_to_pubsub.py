import json
import os
import time
from google.cloud import pubsub_v1

credentials_path = "de-project-pubsub.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path


# Verileri içeren CSV dosyasını okuyun
csv_data = []
with open('homes.csv', 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip().split(',')  # Başlıkları al
    for line in lines[1:]:  # Başlıkları atla
        csv_data.append(line.strip().split(','))

# JSON formatına dönüştürme fonksiyonu
def convert_to_json(data, headers):
    json_data = []
    for row in data:
        json_row = {}
        for i, value in enumerate(row):
            if value:  # Boş değerleri kontrol et
                json_row[headers[i]] = float(value) if '.' in value else int(value)
        json_data.append(json_row)
    return json_data

# PubSub'a gönderme fonksiyonu
def send_to_pubsub(data):
    project_id = 'de-project-389718'
    topic_id = 'python-to-pubsub'
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    for row in data:
        message_data = json.dumps(row).encode('utf-8')
        future = publisher.publish(topic_path, message_data)
        print(f'Message published: {future.result()}')

        time.sleep(10)  # 10 saniye aralıkla gönder

# Verileri JSON formatına dönüştür
json_data = convert_to_json(csv_data, headers)

# JSON verilerini PubSub'a gönder
send_to_pubsub(json_data)
