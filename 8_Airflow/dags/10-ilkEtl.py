from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import requests #apiden veri almak için
import json #apiyi json formatına dönüş. için
from datetime import datetime
import os #dosyalar ile çalışmak için "operating system"
from google.cloud import storage #gcs'a bağlanmak için

def get_api():
    

with DAG(
    dag_id="16_ilk_etl",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    )as dag:

    ilk_task=PythonOperator(
        task_id="ilk_task",
        python_callable=get_api
    )

    ilk_task
