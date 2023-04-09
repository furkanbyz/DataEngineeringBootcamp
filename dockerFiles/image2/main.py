from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"hello world, hello everyone!"}