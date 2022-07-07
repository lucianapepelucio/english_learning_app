from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

users = [
    {"id": 1, "username": "Luciana", "password": "123456"},
    {"id": 2, "username": "Maria", "password": "2345vlw"},
    {"id": 3, "username": "Carlos", "password": "654321"},
    {"id": 4, "username": "Marcos", "password": "canguru123"}
]

def find_next_id():
    i = 0
    for user in range(users.length):
        users.append(i)
        i +=1
        return user

class User(BaseModel):
    id: int = Field(default_factory=find_next_id)
    username: str
    password: str


@app.get("/")
async def main():
    return("English Learning App")


@app.get("/users")
async def get_users_list():
    return {'Users List': users}


@app.get("/users/{id}")
async def get_user(id: int, user: User):
    if user.id in users:
        return {'User': user}
    else:
        return {'Error': 'User not found!'}


@app.post("/users")
async def add_user(user: User):
    users.append(user)
    return user

