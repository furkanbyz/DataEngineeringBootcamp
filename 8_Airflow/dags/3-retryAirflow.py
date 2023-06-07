from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from datetime import timedelta



with DAG(
    dag_id="6_retry",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    ) as dag:

    ilk_task = BashOperator(
        task_id ="ilk_task",
        retries = 3,
        #yapı 3 kere tekrar etsin
        retry_delay = timedelta(seconds=10),
        #10sn'de bir tekrar etsin
        bash_command="python deneme.py"
    )

    ilk_task

#bu komutla 3 kere deneyip tamamında fail edip işlemi bitirir