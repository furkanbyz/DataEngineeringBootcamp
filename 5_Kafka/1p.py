from kafka import KafkaProducer

p = KafkaProducer(bootstrap_servers="localhost:9092")

p.send("ornek",b'derse hos geldiniz')
p.flush()