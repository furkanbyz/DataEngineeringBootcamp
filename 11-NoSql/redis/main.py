from fastapi import FastAPI

import redis
r = redis.Redis(host="localhost",port=6379,db=0)



app = FastAPI()

@app.get("/users/{user_id}")
def users(user_id:str):
    user_name = r.get(user_id)
    
    return {"user_id":user_id,"user_name":user_name}


@app.post("/users/{user_id}/{user_name}")
def cereate_users(user_id:str,user_name:str):
    r.set(name=user_id,value=user_name)
    return {"mesaj gönderildi"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)