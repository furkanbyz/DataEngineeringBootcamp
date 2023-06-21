from airflow import DAG
import pendulum
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.contrib.operators.postgres_to_gcs_operator import PostgresToGoogleCloudStorageOperator

# Postgre to GCS, from here to Bigquery

PROJE_AD = "qualified-ace-386113"
DB_AD = "ders"


with DAG(
    dag_id="19_PostgreToBigQuery",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    ) as dag:

    #Postgres veritabanından Google Cloud Storage'a veri aktarmak için operatörü yapılandırıyoruz:
    #Bu operatör, baglanti_postgre adlı Postgres bağlantı kimliğini kullanarak 
    #my_table tablosundaki id, name ve age sütunlarını seçen bir SQL sorgusunu çalıştırır 
    #ve sonuçları veriler.csv dosyası olarak postgretobigqery adlı Google Cloud Storage bucketine aktarır.
    postgretogcs = PostgresToGoogleCloudStorageOperator(
        task_id = "postgretogcs",
        postgres_conn_id="baglanti_postgre",
        sql = "select id ,name ,age from my_table",
        bucket = "postgretobigquery",
        filename = "veriler.csv" #kaydedirken kullanması istenilen isim
    )

    #GCSToBigQueryOperator operatörü ile GCS'den BigQuery'ye veri aktarmayı yapılandırıyoruz:
    #Bu operatör, postgretobigquery adlı Google Cloud Storage bucketindeki veriler.csv dosyasından veriyi çeker
    #ve NEWLINE_DELIMITED_JSON formatında olduğunu belirtir. İlk satırı atlar, alanları (kolonları) virgülle ayırarak okur.
    #Ardından, veriyi {PROJE_AD}.{DB_AD}.postgretogcs adlı BigQuery proje-veri kümesi-tablosuna yazar. 
    # Tablo oluşturma ve yazma ayarlamaları da yapılmıştır.
    load_data = GCSToBigQueryOperator(
        task_id = "load_data",
        bucket="postgretobigquery",
        source_objects="veriler.csv",
        source_format="NEWLINE_DELIMITED_JSON",
        skip_leading_rows=1,
        field_delimiter=",",
        destination_project_dataset_table=f"{PROJE_AD}.{DB_AD}.postgretogcs",
        create_disposition="CREATE_IF_NEEDED", 
        write_disposition="WRITE_TRUNCATE",
        # WRITE_EMPTY
        # WRITE_APPEND
        # WRITE_TRUNCATE
        gcp_conn_id="google_cloud_default"
    )


    postgretogcs >> load_data 