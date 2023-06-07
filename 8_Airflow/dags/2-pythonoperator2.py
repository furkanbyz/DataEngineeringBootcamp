from airflow import DAG
#Apache Airflow, iş akışlarını programlamak ve yönetmek için açık kaynaklı bir platformdur.
#DAG (Directed Acyclic Graph), Apache Airflow'da bir iş akışını temsil eden bir Python sınıfıdır. İş akışının adımlarını ve bağımlılıklarını tanımlar.
from airflow.operators.python import PythonOperator

import pendulum
# Pendulum, Python dilinde tarih ve saatle ilgili gelişmiş bir kütüphanedir. Tarihleri ve saatleri temsil etmek, manipüle etmek ve arasındaki farkları hesaplamak için kullanılabilir

#https://crontab.guru/ incele

#airflow taskları içindeki XCOM kısmıyla ilgili işlemler yapıldı
#tüm print ve return fonksiyonlar birer veri tutar XCOM'lar ile.

def ilk_fonk():
    return "furkan"

def deger_alan(soyisim, ti):
    isim = ti.xcom_pull("ilk_task")
    #ilk_task adlı tasktan veriyi çekiyor. O task ise veriyi ilk_fonk adlı fonksiyondan alıyor (return "furkan")
    
    print(f"merhaba{isim}{soyisim}")
    #ti airflow'a özel bir şeydir ve fonksiyonlar arasında veri aktarımını sağlar

with DAG(
    dag_id= "4_python_2",
    schedule= "@daily",
    start_date= pendulum.datetime(2023,5,31, tz="UTC")
    )    as dag:

    ilk_task = PythonOperator(
        task_id = "ilk_task",
        python_callable=ilk_fonk
        #yukarıda tanımlanan fonksiyon bu şekilde çağrıldı
    )

    ikinci_task = PythonOperator(
        task_id = "ikinci_task",
        python_callable=deger_alan,
        #yukarıda tanımlanan fonksiyon bu şekilde çağrıldı

        op_kwargs={"isim":"furkan", "soyisim":"beyaz"}
        #değer alan bir fonksiyona bu şekilde dışarıdan değer verdik
    )

    ilk_task >> ikinci_task

#kod tamamlandığında terminale "python -m venv airflow_env" ile airflow environment'ı oluştur
#tepki vermezse ".\airflow_env\Scripts\activate" ile aktif et