from fastapi import FastAPI, Depends
from pydantic import BaseModel
# pydantic hem hızlı çalışmasını, 
# basemodel de daha düzenli(istenilen türde veri için) veri akışı için
import psycopg2

app = FastAPI()
# get, post, put, delete

def get_connection():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgre",
        host="localhost",
        port="5432"
    )
    return conn


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
    return rows


@app.get("/get-user/{user_id}")
def get_user(user_id:int,baglanti = Depends(get_connection)):
    try:
        cursor = baglanti.cursor()
        cursor.execute("Select * from users where id = %s",(user_id,))
        row = cursor.fetchone()
        
    except:
        return {"hata":"Bağlantı oluşturulamadı"}
    
    finally:
        baglanti.close()

    if not row:
        return {"bilgi": "Böyle bir kullanıcı yok"}
    
    return row


class User(BaseModel):
    name: str
    email: str
    phone: int


@app.post("/users")
def create_user(user:User, conn = Depends(get_connection)):
    try:
        cursor=conn.cursor()
        cursor.execute("SELECT phone FROM users WHERE phone = %s",(user.phone,))
        row = cursor.fetchone()
        if row:
            return {"detail": "Böyle bir telefon numarası daha önce eklendi"}  
        
        cursor.execute("INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)",(user.name, user.email, user.phone))
        
        conn.commit()

    except Exception:
        return {"hata":"Bağlantı oluşturulamadı"}
    finally:
        conn.close()
    return {"success": True}







@app.get("/")
def hello():
    return "Hoş Geldiniz"


@app.get("/merhaba")
def hello():
    return "Merhaba"
