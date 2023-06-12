from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta


with DAG(
    dag_id="10_dinamikdag",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    ) as dag:

    dosyalar = ["a","b","c","d","e","f"]

    for dosya in dosyalar:
        extract = BashOperator(
            task_id =f"extract_{dosya}",
            bash_command="echo ilk airflow taskımı olusturdum"
             )
        
        transform = BashOperator(
            task_id =f"transform_{dosya}",
            bash_command="echo ilk airflow taskımı olusturdum"
             )
        
        load = BashOperator(
            task_id =f"load_{dosya}",
            bash_command="echo ilk airflow taskımı olusturdum"
             )
        extract >> transform >> load
