from google.cloud import pubsub_v1
import json
import os
import pandas as pd
import time

credentials_path = "de-project-pubsub.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

proje_id = "de-project-389718"
topic_name = "python-to-pubsub"

publisher = pubsub_v1.PublisherClient()
topic_adres = publisher.topic_path(proje_id,topic_name)

df = pd.read_csv("homes.csv")

for _, row in df.iterrows():
    to_json = row.to_dict()
    time.sleep(1)
    

    gonder = publisher.publish(topic_adres, json.dumps(to_json).encode("utf-8"))
    print(f"Mesaj Id si : {gonder.result()}")