from fastapi import FastAPI, Depends
# Depends ile sanal ortama girildiğinde otomatik olarak db'ye bağlanılır
from pydantic import BaseModel
# BaseModel, verilerin belli standartlarda gelmesini sağlar
import psycopg2

app = FastAPI()

# get post put delete

@app.get("/")
def hello():
    return "Hoş Geldiniz"

@app.get("/merhaba")
def merhaba():
    return "Merhaba"