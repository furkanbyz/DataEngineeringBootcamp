from google.cloud import pubsub_v1
import os

proje_id = "qualified-ace-386113"
topic_name = "de_subat_gcs_to_pubsub"
mesaj = "yeni çalışmadan selamlar"

publisher = pubsub_v1.PublisherClient()

topic_address = publisher.topic_path(proje_id, topic_name)

gonder = publisher.publish(topic_address, data=mesaj.encode("utf-8"))

