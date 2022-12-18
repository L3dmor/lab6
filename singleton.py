class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, username, login, password):
        self.username = username
        self.login = login
        self.password = password


if __name__ == "__main__":
    db1 = DataBase('user1', 'user1', 'qwerty123')
    db2 = DataBase('user2', 'user2', 'qwerty123')
    print(db1 is db2)
