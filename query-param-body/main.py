
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id : int
    name : str
    age : int


@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(user: User):
    users.append(user)
    return {
        "message": "User added successfully",
        "data" : users
    }


@app.put("/users/{user_id}")
def update_user(user_id : int, update_user : User, notify : bool = False):
    for index , user in enumerate(users):
        if user.id == user_id:
            users[index] = update_user
            return {
                "message" : "User updated successfully",
                "data" : users,
            }
    return {
        "error" : "User not found "
    }