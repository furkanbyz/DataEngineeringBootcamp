from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG(
    dag_id="14_postgre",
    schedule="@daily",
    start_date=pendulum.datetime(2022,5,20,tz="UTC"),
    catchup=False
    #geriye dönüş işlemlere bakmaz

    ) as dag:

    create_table = PostgresOperator(
        task_id = "create_table",
        postgres_conn_id="baglanti_postgre",

        sql = """
            create table if not exists dag_runs(
                    tarih date,
                    dag_id character varying
                )        
                """
        )
    
    instert_table = PostgresOperator(
        task_id = "instert_table",
        postgres_conn_id="baglanti_postgre",

        sql = """
            insert into dag_runs (tarih,dag_id) values ('{{ ds }}', '{{ dag.dag_id}}')
        
        """
    )
    #https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html#variables incele
    #dag.dag_id ile dag adını verir
    #ds: The DAG run’s logical date
    create_table >> instert_table
    
        