from airflow import DAG
#Apache Airflow, iş akışlarını programlamak ve yönetmek için açık kaynaklı bir platformdur.
#DAG (Directed Acyclic Graph), Apache Airflow'da bir iş akışını temsil eden bir Python sınıfıdır. İş akışının adımlarını ve bağımlılıklarını tanımlar.
from airflow.operators.bash import BashOperator
# BashOperator, Apache Airflow'da bir işlemi temsil eden bir operatördür. BashOperator, bir bash komutunu çalıştırmak için kullanılır.
import pendulum
# Pendulum, Python dilinde tarih ve saatle ilgili gelişmiş bir kütüphanedir. Tarihleri ve saatleri temsil etmek, manipüle etmek ve arasındaki farkları hesaplamak için kullanılabilir

#https://crontab.guru/ incele

#airflow taskları içindeki XCOM kısmıyla ilgili işlemler yapıldı
#tüm print ve return fonksiyonlar birer veri tutar XCOM'lar ile.

with DAG(
    dag_id= "2_bash_2",
    schedule= "@daily",
    start_date= pendulum.datetime(2023,5,31, tz="UTC")
    )    as dag:

    ilk_task = BashOperator(
        task_id = "ilk_task",
        bash_command="python /opt/airflow/dags/scripts/deneme.py",
        do_xcom_push= False
        #False ile herhangi bir XCOM verisi tutmadan işlem yapmasını istedik
    )

    ilk_task

#kod tamamlandığında terminale "python -m venv airflow_env" ile airflow environment'ı oluştur
#tepki vermezse ".\airflow_env\Scripts\activate" ile aktif et