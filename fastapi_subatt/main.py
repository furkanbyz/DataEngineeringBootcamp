from fastapi import FastAPI, Depends
# Depends ile sanal ortama girildiğinde otomatik olarak db'ye bağlanılır
from pydantic import BaseModel
# BaseModel, verilerin belli standartlarda gelmesini sağlar
import psycopg2
# postgresql için

app = FastAPI()
# get post put delete işlemleri yapılabilir

# postgresql bağlantısı yapıldı
def get_connection():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgre",
        host="localhost",
        port="5432"
    )
    return conn

@app.get("/")
def hello():
    return "Hoş Geldiniz"

@app.get("/merhaba")
def merhaba():
    return "Merhaba"

@app.get("/get-users")
def get_users(baglanti = Depends(get_connection)):
    try:
        cursor = baglanti.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
    except:
        return {"hata":"bağlantı oluşturulamadı"}
    finally:
        baglanti.close()