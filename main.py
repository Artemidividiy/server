
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
                return i[0]
        return status.HTTP_400_BAD_REQUEST

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
    scheme = SchemeController().postScheme(scheme=schema)
    return scheme.id


@app.post("/schema", status_code=status.HTTP_403_FORBIDDEN)
async def post_schema_without_auth():
    return "bad request"

@app.post("/like/{schema_id}/{user_id}")
async def like_schema(schema_id: int, user_id: int):
    user_controller = UserController()
    schema_controller = SchemeController()
    schema_controller.like_schema(user_id, scheme=schema_id)
    return "200"

if __name__ == "__main__":
    exec("uvicorn main:app --reload")