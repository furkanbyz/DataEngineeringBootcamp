from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
import requests #apiden veri almak için
import json #apiyi json formatına dönüş. için
from datetime import datetime
import os #dosyalar ile çalışmak için "operating system"
from google.cloud import storage #gcs'a bağlanmak için

def get_api():
    # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/opt/8_Airflow/dags/scripts/qualified-ace-386113-5d71d69ce746.json'

    dag_directory = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(dag_directory, 'scripts', 'qualified-ace-386113-5d71d69ce746.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    url_lik = "http://api.weatherapi.com/v1/current.json"
    access_key = "fe661b56017447dab3d24625220704"

    iller = ["istanbul","ankara","Malatya"]
    gecici_hafiza = []


    for il in iller:
        response = requests.get(url=url_lik,params={"key":access_key,"q": f"{il}"}).json()

        deger = {
            "il":response["location"]["region"],
            "sicaklik":response["current"]["temp_c"]
        }
        gecici_hafiza.append(deger)


    tarih = datetime.now()

    simdi = tarih.strftime("%Y")+ "_"+tarih.strftime("%m") +"_"+tarih.strftime("%d") +"_"+tarih.strftime("%H") +"_"+tarih.strftime("%M")  +"_"+tarih.strftime("%S") 
    #strftime ile karışık saat tarih yapıları parçalanabilir
    dosya_adi = f"veri-{simdi}.json"

    client = storage.Client()

    bucket = client.bucket("airflow-lecture")
    #gcp üzerindeki bucket ismi, bu bucket'e veri yüklenecek

    veriler_json = json.dumps(gecici_hafiza).encode("utf-8")
    #gecici_hafiza içindeki veriler buraya kaydedilsin

    blob = bucket.blob(dosya_adi)
    #bir dosya oluşturuldu
    blob.upload_from_string(veriler_json)
    #oluşturulan dosyaya veriler yüklendi


with DAG(
    dag_id="16_ilk_etl",
    schedule="@daily",
    #zamanlama için, https://crontab.guru/#*_*_*_*_*_7
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    )as dag:

    ilk_task=PythonOperator(
        task_id="ilk_task",
        python_callable=get_api
    )

    ilk_task
