from airflow.decorators import dag
from airflow.operators.bash import BashOperator
import pendulum

@dag(
    dag_id="11_task",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
)
#decorators kullanılarak task oluşturuldu

def ilk_task_dag():
    bash_task1= BashOperator(
        task_id="bash_task1",
        bash_command="echo ilk airflow taskımı olusturdum"
    )
    bash_task2= BashOperator(
        task_id="bash_task2",
        bash_command="echo ilk airflow taskımı olusturdum"
    )
    bash_task1 >> bash_task2
    
ilk_task_dag()
#def ile oluşturulan fonksiyon burada çağırıldı