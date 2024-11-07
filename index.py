from fastapi import FastAPI
from routes.user import user 


app = FastAPI()
app.include_router(user)

@app.get('/')
def home():
    return {"message":"hello world"}
