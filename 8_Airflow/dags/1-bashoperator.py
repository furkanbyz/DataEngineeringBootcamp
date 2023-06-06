from airflow import DAG
#Apache Airflow, iş akışlarını programlamak ve yönetmek için açık kaynaklı bir platformdur.
#DAG (Directed Acyclic Graph), Apache Airflow'da bir iş akışını temsil eden bir Python sınıfıdır. İş akışının adımlarını ve bağımlılıklarını tanımlar.
from airflow.operators.bash import BashOperator
# BashOperator, Apache Airflow'da bir işlemi temsil eden bir operatördür. BashOperator, bir bash komutunu çalıştırmak için kullanılır.
import pendulum
# Pendulum, Python dilinde tarih ve saatle ilgili gelişmiş bir kütüphanedir. Tarihleri ve saatleri temsil etmek, manipüle etmek ve arasındaki farkları hesaplamak için kullanılabilir

#https://crontab.guru/ incele

with DAG(
    dag_id= "1_bash_1",
    schedule= "@daily",
    start_date= pendulum.datetime(2023,5,31, tz="UTC")
    )    as dag:

    ilk_task = BashOperator(
        task_id = "ilk_task",
        bash_command="echo ilk airflow taskımı olusturdum"
    )

    ilk_task

#kod tamamlandığında terminale "python -m venv airflow_env" ile airflow environment'ı oluştur
#tepki vermezse ".\airflow_env\Scripts\activate" ile aktif et