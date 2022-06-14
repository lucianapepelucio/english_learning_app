from fastapi import FastAPI
from pydantic import BaseModel, Field  

app = FastAPI()

def find_user_id():
    return max(user.user_id for user in users) + 1
class User(BaseModel):
    user_id: int = Field(default_factory=find_user_id, alias="id")
    name: str
    password: str

users = [
    {"id": 1, "name": "Luciana", "password": "123456"},
    {"id": 2, "name": "Maria", "password": "2345vlw"},
    {"id": 3, "name": "Carlos", "password": "654321"},
    {"id": 4, "name": "Marcos", "password": "canguru123"}
]

@app.get("/")
async def main():
    return("English Learning App")

@app.get("/users", status_code=200)
async def get_users_list():
    return users

@app.get("/users/{user_id}", status_code=200)
async def get_user(user_id: int):
    search = list(filter(lambda x: x["id"] == user_id, users))

    if search == []:
        return {'Error': 'User not found!'}

    return {'User': search[0]}

@app.post("/users", status_code=201)
async def add_user(user: User):
    users.append(user)
    return user

# @app.get("/users/{user_name}")
# async def get_user(user_name: str):
#     search = list(filter(lambda x: x["name"] == user_name, users))

#     if search == []:
#         return {'Error': 'User not found'}

#     return {'User': search[0]}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}

# Criar 
# @app.put com id
# @app.delete com id
# @app.patch com id
