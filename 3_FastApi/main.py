from fastapi import FastAPI, Depends
# Depends ile sanal ortama girildiğinde otomatik olarak db'ye bağlanılır
from pydantic import BaseModel
# BaseModel, verilerin belli standartlarda gelmesini sağlar
import psycopg2
# postgresql için
from typing import Optional

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
    return rows



@app.get("/get-user/{user_id}")
def get_user(user_id:int , baglanti = Depends(get_connection)):
    try:
        cursor = baglanti.cursor()
        cursor.execute("select * from users where id=%s",(user_id,))
        row = cursor.fetchall()
    except:
        return {"hata":"bağlantı oluşturulamadı"}
    finally:
        baglanti.close()

    if not row:
        return {"detail":"böyle bir kullanıcı yok"}
    
    return row



class User(BaseModel):
    name:str
    email:str
    phone:int

@app.post("/users")
def create_user(user:User, conn = Depends(get_connection)):
    try:
        cursor = conn.cursor()
        cursor.execute("select phone from users where id=%s",(user.phone,))
        row = cursor.fetchone()

        if row:
            return {"detail":"böyle bir numara daha önce eklendi"}
        cursor.execute("insert into users (name,email,phone) values (%s,%s,%s)",(user.name, user.email, user.phone))
        conn.commit()

    except:
        return {"hata":"bağlantı oluşturulamadı"}
    
    finally:
        conn.close()

    return {"success":True}


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, conn=Depends(get_connection)):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT phone FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()

        if not row:
            return {"detail": "Böyle bir kullanıcı yok"}

        set_clause = ""
        values = []
        if user.name is not None:
            set_clause += "name = %s, "
            values.append(user.name)
        if user.email is not None:
            set_clause += "email = %s, "
            values.append(user.email)
        if user.phone is not None:
            set_clause += "phone = %s, "
            values.append(user.phone)
        set_clause = set_clause.rstrip(", ")

        cursor.execute(
            f"UPDATE users SET {set_clause} WHERE id = %s",
            (*values, user_id),
        )
        conn.commit()
    except:
        return {"hata": "Bağlantı oluşturulamadı"}
    finally:
        conn.close()

    return {"success": True}



@app.delete("/users/{user_id}")
def delete_user(user_id: int, conn = Depends(get_connection)):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT phone FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()

        if not row:
            return {"detail": "Böyle bir kullanıcı yok"}

        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
    except:
        return {"hata": "Bağlantı oluşturulamadı"}
    finally:
        conn.close()

    return {"success": True}


