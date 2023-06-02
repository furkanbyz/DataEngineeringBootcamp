from google.cloud import pubsub_v1
import json
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'qualified-ace-386113-bee8829f02bd.json'
def publish_message(project_id, topic_name, message):
    # Pub/Sub istemcisini oluştur
    publisher = pubsub_v1.PublisherClient()
    
    # Mesaj verisini JSON formatına dönüştür
    message_data = json.dumps(message).encode('utf-8')
    
    # Mesajı Pub/Sub'a gönder
    topic_path = publisher.topic_path(project_id, topic_name)
    future = publisher.publish(topic_path, data=message_data)
    future.result()
    
    print('Mesaj Pub/Sub\'a başarıyla gönderildi.')

# Pub/Sub proje ID'si
project_id = 'qualified-ace-386113'

# Mesaj gönderilecek topic adı
topic_name = 'tobigquery'

# Gönderilecek mesaj verisi
message = {
    'ad': 'kerem',
    'soyad': 'beyaz'
}

# Mesajı Pub/Sub'a gönder
publish_message(project_id, topic_name, message)