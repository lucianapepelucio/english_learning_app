from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

users = [
    {"id": 1, "username": "Luciana", "password": "123456"},
    {"id": 2, "username": "Maria", "password": "2345vlw"},
    {"id": 3, "username": "Carlos", "password": "654321"},
    {"id": 4, "username": "Marcos", "password": "canguru123"}
]

# def find_next_id():
#     for i in range(len(users)):
#         users.append(i)
#         i +=1
#         return i      percorrer todo o array e adicionar 1 ao último

class User(BaseModel):
    # id: int = Field(default_factory=find_next_id)
    id: int
    username: str
    password: str


@app.get("/")
async def main():
    return("English Learning App")


@app.get("/users")
async def get_users_list():
    return {'Users List': users}


@app.get("/users/{id}")
async def get_user(id: int):
    for user in users:
        if id == user["id"]:
            return {'User': user}
        else:
            return {'Error': 'User not found!'}


@app.post("/users")
async def add_user(user: User):
    users.append(user)
    return user


@app.put("/users/{id}")
async def update_user(
    id: int = Path(title="Pegar o id do usuário a ser atualizado"), 
    username: str = Query(default=None), 
    password: str = Query(default=None)
):
    user = {"id": id}
    
    if username:
        user.update({"username": username})
    if password:
        user.update({"password": password})
    return {'User': user}
