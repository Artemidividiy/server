import json
from models.user import UserBase, UserModel
from services.postgresDefault import PostgreServiceDefault
from psycopg2 import sql


class UserController:
    def __init__(self) -> None:
        self.pg = PostgreServiceDefault()

    def getUsers(self, id=None) -> list[UserModel] | UserModel | None:
        users = self.pg.execute("select * from user_view", vars=())
        print(users)
        if id == None:
            print(json.dumps(users))
            return users
        else:
            for i in users:
                if i[0] == id:
                    return i

    def postUser(self, user: UserModel):
        self.pg.execute("INSERT INTO public.users(password, email) values (%s, %s)",
                        (user.password, user.email))
        user.id = self.pg.execute(
            "select id from public.users order by id desc limit 1", vars=())
        print(user)
        return user
