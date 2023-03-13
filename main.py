
import json
from api.root import api_main
from fastapi import FastAPI, status
from controllers.scheme import SchemeController
from controllers.user import UserController
from models.scheme import SchemeModel

from models.user import UserModel


app = FastAPI()

@app.get("/root")
async def root(): 
    return "this is a root"

@app.post("/user")
async def authenticate_user(user: UserModel):
    controller = UserController()
    print(user)
    if(user.authorized == False):
        user = controller.postUser(user)
        return user.id
    else:
        users = controller.getUsers()
        for i in users:
            if i[1] == user.email:
                if i[2] == user.password: 
                    return i[0]
                else: return "wrong password"
        return "not found"

@app.get("/schema/{user_id}")
async def get_schema(user_id: int):
    schemas = SchemeController().getSchemas()
    user = UserController().getUsers(id=user_id)
    for i in schemas: 
        print(i)

@app.get("/schema/", status_code=status.HTTP_403_FORBIDDEN)
async def get_schema_without_auth():
    return "bad request"

@app.post("/schema/{user_id}")
async def post_schema(user_id: int, schema: SchemeModel):
    print(schema)
    scheme = SchemeController().postScheme(scheme=schema)
    return scheme.id


@app.post("/schema", status_code=status.HTTP_403_FORBIDDEN)
async def post_schema_without_auth():
    return "bad request"

@app.post("/like/{schema_id}/{user_id}")
async def like_schema(schema_id: int, user_id: int):
    
    schema_controller = SchemeController()
    schema_controller.like_schema(user_id, scheme_id=schema_id)
    return "200"

@app.post("/dislike/{schema_id}/{user_id}")
async def dislike_schema(schema_id: int, user_id: int):
    
    schema_controller = SchemeController()
    schema_controller.dislike_schema(user_id, scheme_id=schema_id)
    return "200"

@app.get("/liked/{user_id}", )
async def liked_schemas(user_id: int):
    schema_controller = SchemeController()
    schemas = schema_controller.user_liked(user_id=user_id)
    return schemas
