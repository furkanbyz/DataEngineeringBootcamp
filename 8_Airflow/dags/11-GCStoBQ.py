from airflow import DAG
import pendulum
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator



PROJE_AD = "qualified-ace-386113" # proje ıd
DB_AD = "ders" # bigquery'de kullanılacak olan db adı


with DAG(
    dag_id="18_GCSToBigQuery",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    ) as dag:
    
    #Configuring the operator to load data from GCS to BigQuery:
    load_data = GCSToBigQueryOperator(
        task_id = "load_data",
        bucket="bigquery_json",
        source_objects="uber_data.csv",
        source_format="CSV",
        skip_leading_rows=1,
        field_delimiter=",",#csv'deki dataları virgül ile ayırır
        destination_project_dataset_table=f"{PROJE_AD}.{DB_AD}.butun_veri1",
        create_disposition="CREATE_IF_NEEDED", #böyle bir yapı yoksa oluşturur
        write_disposition="WRITE_TRUNCATE",
        # WRITE_EMPTY : sürekli aynı veriyi tablonun altına ekler
        # WRITE_APPEND : öyle bir tablo yoksa oluşturur varsa hata verir
        # WRITE_TRUNCATE : tablo yoksa oluşturur varsa da verilerin tamamını silip yenisini yazar
        gcp_conn_id="google_cloud_default" # airflow - admin - connections menüsünde oluşturulan connection id
    )

    #Veri analizi için bir SQL sorgusu tanımlıyoruz: 
    #Bu sorgu, butun_veri1 tablosundaki tip_amount sütunu 3.3'ten büyük olan tüm satırları seçer.
    sorgu =f"Select * from {PROJE_AD}.{DB_AD}.butun_veri1 where tip_amount > 3.3"

    #BigQuery'de yeni bir tablo oluşturmak için sorguyu çalıştırıyoruz:
    create_new_table = BigQueryExecuteQueryOperator(
        task_id = "create_new_table",
        sql=sorgu,
        destination_dataset_table=f"{PROJE_AD}.{DB_AD}.butun_veri_analiz",
        create_disposition="CREATE_IF_NEEDED", 
        write_disposition="WRITE_TRUNCATE",
        use_legacy_sql=False,
        gcp_conn_id="google_cloud_default"
    )


    load_data >> create_new_table