class User:
    def __init__(self, username: str, email: str, password: str):
        self.__username = username
        self.__email = email
        self.__password = password

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email


class PremiumUser(User):
    pass


class GuestUser(User):
    pass

