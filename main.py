
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
    if(user.authorized == False):
        controller.postUser(user)
    else:
        users = controller.getUsers()
        for i in users:
            if i[1] == user.username:
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
    SchemeController().postScheme(scheme=schema, user_id=user_id)


@app.post("/schema", status_code=status.HTTP_403_FORBIDDEN)
async def post_schema_without_auth():
    return "bad request"


if __name__ == "__main__":
    exec("uvicorn main:app --reload")