from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sql import BranchSQLOperator

import pendulum


create_table_sql = '''
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER
        );
    '''

insert_data_sql = '''
    INSERT INTO my_table (name, age) VALUES ('ahmet', 25), ('mehmet', 30), ('mustafa', 40);
'''

with DAG(
    dag_id="16_brenchSql",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")

) as dag:
    create_table_task = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='baglanti_postgre',
        sql=create_table_sql
    )

    insert_data_task = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='baglanti_postgre',
        sql=insert_data_sql
    )

    check_data_task = BranchSQLOperator(
        task_id='check_data',
        conn_id='baglanti_postgre',
        #sql="select age from my_table where age > 600;",
        sql="SELECT CASE WHEN EXISTS (SELECT 1 FROM my_table WHERE age > 600) THEN 1 ELSE 0 END;",

        follow_task_ids_if_true='data_greater_than_5_true',
        follow_task_ids_if_false='data_less_than_or_equal_to_5_false'
    )

    data_greater_than_5_task = DummyOperator(
        task_id='data_greater_than_5_true',
        dag=dag
    )

    data_less_than_or_equal_to_5_task = DummyOperator(
        task_id='data_less_than_or_equal_to_5_false',
        dag=dag
    )



    create_table_task >> insert_data_task >> check_data_task >>[data_greater_than_5_task,data_less_than_or_equal_to_5_task]
