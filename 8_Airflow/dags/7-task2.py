from airflow.decorators import dag,task
from airflow.operators.bash import BashOperator
import pendulum

#dag, gün içinde çalışan bir iş akışı olarak düşünülebilir
@dag(
    dag_id="11_task2",
    schedule="@daily",
    start_date=pendulum.datetime(2023,5,31,tz="UTC")
    #hangi tarihte başlayacağı belirtildi
)
#decorators kullanılarak task oluşturuldu

def ilk_task_dag():

    @task(multiple_outputs=True)
    def bilgiler():
        return{
            "isim":"furkan",
            "soyad":"beyaz"
        }
    
    @task()
    def yas():
        return 23
    
    @task()
    def birlestir(isim,soyad,yas):
        print(f"{isim}{soyad}{yas}")
    
    bilgi_val = bilgiler()
    yas_val = yas()

    birlestir(isim= bilgi_val["isim"], soyad= bilgi_val["soyad"], yas= yas_val)


#python fonksiyonları airflow task'ı gibi gösterildi
    

ilk_task_dag()
#def ile oluşturulan fonksiyon burada çağırıldı