from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pickle # model kaydetmek için
import pandas as pd
import logging
import seaborn as sns
import matplotlib.pyplot as plt # görselleştirmeler için
from sklearn.metrics import accuracy_score, precision_score, recall_score
from airflow.providers.postgres.operators.postgres import PostgresOperator


# Veri işleme işlevi
def preprocess_data(ti):
    try:
        # Veri setini yükle
        df = pd.read_csv('../data/diabet.csv')

        # Veri ön işleme adımlarını gerçekleştir
        # Örnek olarak eksik değerleri doldurma
        df.fillna(0, inplace=True)

        # Ön işlenmiş veriyi başka bir dosyaya kaydet
        df.to_csv('/opt/airflow/dags/data/preprocessed_diabet.csv', index=False)

        logging.info("Veri ön işleme tamamlandı.")
        ti.xcom_push(key='dataset_name', value="diabet.csv")

    except Exception as e:
        logging.error("Veri ön işleme hatası: %s", str(e))


# Eğitim işlevi
def train_model(ti):
    try:
        # Ön işlenmiş(yukarıda düzenlenen veriler) veri setini yükle
        df = pd.read_csv('/opt/airflow/dags/data/preprocessed_diabet.csv')

        # Veri setini özellikler (X) ve hedef (y) olarak ayır
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']

        # Makine öğrenimi modelini eğit
        # Örnek olarak bir Lojistik Regresyon modeli kullanma
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        model.fit(X, y)

        # Eğitilmiş modeli kaydet
        with open('/opt/airflow/dags/models/diabetes_model.pkl', 'wb') as file:
            pickle.dump(model, file)

        logging.info("Model eğitimi tamamlandı.")
        ti.xcom_push(key='model_file_name', value=f"diabetes_model.pkl")
        ti.xcom_push(key='model_name', value="LogisticRegression")

    except Exception as e:
        logging.error("Model eğitimi hatası: %s", str(e))

# Tahmin işlevi
def make_predictions(ti):
    try:
        # Eğitilmiş modeli yükle
        with open('/opt/airflow/dags/models/diabetes_model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Tahmin yapılacak veriyi yükle
        df = pd.read_csv('/opt/airflow/dags/data/preprocessed_diabet.csv')

        # Tahminleri yap
        X = df.drop('Outcome', axis=1)
        y = df['Outcome']

        predictions = model.predict(X)
        y_pred = model.predict(X)

        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(y, y_pred)
        recall = recall_score(y, y_pred)
        
        ti.xcom_push(key='accuracy', value=accuracy)
        ti.xcom_push(key='precision', value=precision)
        ti.xcom_push(key='recall', value=recall)

        

        logging.info("Tahminler tamamlandı.")
    except Exception as e:
        logging.error("Tahminler hatası: %s", str(e))

# Veri keşfi işlevi
def explore_data():
    try:
        df = pd.read_csv('/opt/airflow/dags/data/diabet.csv')

        # Veri seti hakkında bilgileri göster
        logging.info("Veri seti bilgileri:")
        logging.info(df.info())

        # Özelliklerin dağılımlarını görselleştir ve readme.md'ye ekle
        with open('/opt/airflow/dags/readme.md', 'a') as readme:
            readme.write("## Veri Keşfi Görselleri\n\n")
            for column in df.columns:
                plt.figure(figsize=(8, 6))
                sns.histplot(data=df, x=column)
                plt.title(f"{column} Dağılımı")
                plt.xlabel(column)
                plt.ylabel("Frekans")
                plt.savefig(f'/opt/airflow/dags/plots/{column}_hist.png')  # Görseli kaydet
                #plots klasörünün dizinin kendi dizinine göre düzenle (../plots ?)
                plt.close()  # Görseli kapat

                readme.write(f"### {column} Dağılımı\n\n")
                readme.write(f"![{column} Histogram](plots/{column}_hist.png)\n\n")
                #plots klasörünün dizinin kendi dizinine göre düzenle (../plots ?)

        logging.info("Veri keşfi tamamlandı.")
    except Exception as e:
        logging.error("Veri keşfi hatası: %s", str(e))

# Airflow DAG tanımlaması


dag = DAG('diabetes_mlops_1', schedule_interval="@hourly",start_date= datetime(2023, 6, 3),catchup=False)

# Veri ön işleme işlemi
preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag
)

# Model eğitimi işlemi
train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

# Tahmin işlemi
predict_task = PythonOperator(
    task_id='make_predictions',
    python_callable=make_predictions,
    dag=dag
)


create_table = PostgresOperator(
        task_id = "create_table",
        postgres_conn_id="baglanti_postgre",
        sql = """
        create table if not exists mlmodels(
                dt date,
                dataset_name character varying,
                model_file_name character varying,
                model_name character varying,
                accuracy float8,
                precision float8,
                recall float8
            )        
            """
        )


insert_table_task = PostgresOperator(
    task_id='insert_table',
    postgres_conn_id='baglanti_postgre',

    sql='''
        INSERT INTO mlmodels ( dt, dataset_name,model_file_name,model_name,accuracy,precision,recall ) VALUES (
            '{{ ds }}',
            '{{ ti.xcom_pull(task_ids="preprocess_data",key="dataset_name") }}',
            '{{ ti.xcom_pull(task_ids="train_model",key="model_file_name") }}',
            '{{ ti.xcom_pull(task_ids="train_model",key="model_name") }}',
            '{{ ti.xcom_pull(task_ids="make_predictions",key="accuracy") }}',
            '{{ ti.xcom_pull(task_ids="make_predictions",key="precision") }}',
            '{{ ti.xcom_pull(task_ids="make_predictions", key="recall") }}'
        );
    ''',
    dag=dag
)


# Veri keşfi işlemi
explore_task = PythonOperator(
    task_id='explore_data',
    python_callable=explore_data,
    dag=dag
)

# İşlem sırasını belirleme
preprocess_task >> train_task >> predict_task >> create_table >> insert_table_task>> explore_task