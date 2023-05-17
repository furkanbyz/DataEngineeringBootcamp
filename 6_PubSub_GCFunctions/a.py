from google.cloud import pubsub_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="qualified-ace-386113-c42ff9e1301f.json"
project_id = "qualified-ace-386113" #gcp project id
topic_name = "de_subat_gcs_to_pubsub"

message = "merhaba pubsub"

publisher = pubsub_v1.PublisherClient()
topic_address = publisher.topic_path(project_id,topic_name)

send = publisher.publish(topic_address,data=message.encode("utf-8"))


print(f"Message ID : {send.result()}")
