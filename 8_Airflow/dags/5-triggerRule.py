from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta

with DAG(

    dag_id="8_trigger_1",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31, tz="UTC")
 
)as dag:
    
    extract=BashOperator(
        task_id="extract",
        bash_command="python deneme.py"
    )
    transform1=BashOperator(
        task_id="transform1",
        trigger_rule="all_failed",
        #all_failed ile "senden önce fail varsa sen çalış" dedik
        #fail varsa sonrası çalışmaz
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    transform2=BashOperator(
        task_id="transform2",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    extract >> transform1 >> transform2