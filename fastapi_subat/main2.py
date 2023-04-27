from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional

import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="1273",
        host="localhost",
        port="5432"
    )
    return conn

app = FastAPI()
"""
get-> select
post-> insert
pull-> update
delete-> delete
"""

# / -> ana sayfa 
# @app.get("/")
# def merhaba():
#     return {"mesaj": "hoşgeldiniz"}

# @app.get("/isdsa")
# def isdsa():
#     return {"mesaj": "istdsa mlops hoşgeldiniz"}



@app.get("/get-users")
def get_users(conn = Depends(get_connection)):
    try:
        cursor = conn.cursor()
        cursor.execute("Select * from users")
        rows = cursor.fetchall()
    except:
        return {"hata":"Bağlantı oluşturulamadı"}
    finally:
        conn.close()
    return rows

@app.get("/users/{user_id}")
def get_user(user_id: int, conn = Depends(get_connection)):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
    except:
        return {"hata": "Bağlantı oluşturulamadı"}
    finally:
        conn.close()
    
    if not row:
        return {"detail": "Böyle bir kullanıcı yok"}

    return row


@app.get("/users")
def get_users(phone: Optional[str] = None, conn = Depends(get_connection)):
    try:
        cursor = conn.cursor()
        if phone:
            cursor.execute("SELECT * FROM users WHERE phone = %s", (phone,))
        else:
            cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
    except:
        return {"hata": "Bağlantı oluşturulamadı"}
    finally:
        conn.close()

    return rows

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