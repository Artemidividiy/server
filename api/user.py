from controllers.user import UserController


class UserApi:
    def __init__(self) -> None:
        self.controller = UserController()

    def authenticate(self):
        pass