from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id : int
    name : str

@app.get("/users", response_model = User)
def getusers():
    return {

        "id" : 1,
        "name" : "John Doe",
        "password" : "password123",
    }