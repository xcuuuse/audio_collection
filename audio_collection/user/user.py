from user.authentication import Username, Password
from library.playlist import Playlist


class User:
    def __init__(self, username: Username, email: str, password: Password, playlists: list[Playlist]):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__playlists = playlists

    @property
    def username(self):
        return self.__username.username

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password.password

    @property
    def playlists(self):
        return self.__playlists


class PremiumUser(User):
    def __init__(self, username: Username, email: str, password: Password, playlists: list[Playlist],
                 start_subscription: int):
        super().__init__(username, email, password, playlists)
        self.__start_subscription = start_subscription

    @property
    def start_subscription(self):
        return self.__start_subscription

    def extend_subscription(self, months: int):
        self.__start_subscription += months

    def is_subscription_active(self):
        return self.start_subscription != 0


class GuestUser(User):
    def __init__(self, username: Username, email: str, password: Password, playlists: list[Playlist],
                 session_id: str, access_level: str):
        super().__init__(username, email, password, playlists)
        self.__session_id = session_id
        self.__access_level = access_level

    @property
    def session_id(self):
        return self.__session_id

    @property
    def access_level(self):
        return self.__access_level


class Authentication:
    def __init__(self):
        self.users = {}

    def register(self, name: Username, email: str, password: Password):
        if name.username in self.users:
            print("exists") # MAKE AN EXCEPTION
        new_user = User(name, email, password)
        self.users[name] = new_user
        return new_user

    def log_in(self, username: Username, password: Password):
        user = self.users.get(username)
        if not user:
            return False
        if user.password == password.password:
            return True
        return False

