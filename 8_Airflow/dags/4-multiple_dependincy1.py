from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta

with DAG( 
    dag_id= "7_multiple_1",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31, tz="UTC")
    ) as dag:

    extract= BashOperator(
        task_id="ilk_task",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    transform1= BashOperator(
        task_id="transform1",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    transform2= BashOperator(
        task_id="transform2",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    transform3= BashOperator(
        task_id="transform3",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    load= BashOperator(
        task_id="load",
        bash_command="echo ilk airflow taskımı oluşturdum"
    )
    
    extract >> [transform1,transform2,transform3] >> load
    #transformlar birbirine paralel, extract ve load ise onlara seri bağlandı
   

