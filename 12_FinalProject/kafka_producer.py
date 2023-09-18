from kafka import KafkaProducer

# Kafka üreticiyi başlat
producer = KafkaProducer(bootstrap_servers='kafka_server:9092')

# Veriyi Kafka konusuna gönder
for index, row in df.iterrows():
    message = row.to_json()
    producer.send('finans_verileri', value=message.encode('utf-8'))
