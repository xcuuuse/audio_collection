from user.user import User


class Username:
    def __init__(self, username: str):
        self.__username = username

    @property
    def username(self):
        return self.__username


class Password:
    def __init__(self, password: str):
        self.__password = password


class Authentication:
    def __init__(self, username: Username, password: Password):
        self.__username = username
        self.__password = password

    def register(self, new_user_name: str, email: str, new_user_password: str):
        pass

    def log_in(self, username: Username, password: Password):
        pass

