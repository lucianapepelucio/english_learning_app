from typing import Union
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    password: str

users = [
    {
        'id': 1,
        'name': 'Luciana',
        'password': '123456'
    },
    {
        'id': 2,
        'name': 'Maria',
        'password': '234567'
    },
    {
        'id': 3,
        'name': 'Carlos',
        'password': '654321'
    },
    {
        'id': 4,
        'name': 'Marcos',
        'password': '894561'
    }
]

@app.get("/")
async def read_root():
     return {"English Learning App"}

@app.get("/user/{user_id}")
async def get_user(user_id: int, user: Union[str, None] = None):
    search = list(filter(lambda x: x["id"] == user_id, users))

    if search == []:
        return {'Error': 'Usuário não cadastrado'}

    return {'Usuário': search[0]}

@app.get("/user/{user_name}")
async def get_user(user_name: str, user: Union[str, None] = None):
    search = list(filter(lambda x: x["name"] == user_name, users))

    if search == []:
        return {'Error': 'Usuário não cadastrado'}

    return {'Usuário': search[0]}

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}

# Criar 
# @app.put
# @app.post
# @app.delete
# @app.patch