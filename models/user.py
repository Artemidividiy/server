from pydantic import BaseModel


class UserBase: 
    def __init__(self, username, email, password, id=None) -> None:
        self.id = None
        self.username = username
        self.email = email
        self.password = password

    def to_string(self):
        return f"username: {self.username}\n password: {self.password}\n email: {self.email}\n---\n"


class UserModel(BaseModel):
    id: int | None = None
    username: str
    password: str
    email: str
    authorized: bool | None = False
