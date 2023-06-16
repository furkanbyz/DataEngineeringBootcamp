from airflow import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
import pendulum
import requests



def karar_ver_fonk():
    url_lik = "http://api.weatherapi.com/v1/current.json"
    access_key = "fe661b56017447dab3d24625220704"

    il="istanbul"
    
    response = requests.get(url=url_lik,params={"key":access_key,"q": f"{il}"}).json()

    deger = {
            "il":response["location"]["region"],
            "sıcaklık":response["current"]["temp_c"]
        }    
    
    #apiden yukarıdaki şekilde bilgiler alındı

    if deger["sıcaklık"]>25:
        return "buyuk_deger_task"
    
    elif deger["sıcaklık"] == 15:
        return "esit_deger_task"
    
    else:
        return "dusuk_deger_task"
    #sıcaklık değeri yukarıdaki gibi koşullara bağlandı

with DAG(
    dag_id="15_branchpython",
    schedule="@daily",
    start_date=pendulum.datetime(2022,5,20,tz="UTC"),
    catchup=False
    ) as dag:

    branch_python = BranchPythonOperator(
        task_id = "branch_python",
        python_callable=karar_ver_fonk
    )

    buyuk_deger_task = DummyOperator(task_id="buyuk_deger_task")
    esit_deger_task = DummyOperator(task_id="esit_deger_task")
    dusuk_deger_task = DummyOperator(task_id="dusuk_deger_task")

    load = DummyOperator(
        task_id="load",
        trigger_rule = "one_success"
        )


    branch_python >> [buyuk_deger_task, esit_deger_task, dusuk_deger_task] >> load

