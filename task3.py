import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.logged_in_users = []

    def login(self, username):
        self.logged_in_users.append(username)
        print("User " + username + " logged in successfully.")

    def get_users(self):
        return self.logged_in_users

if __name__ == "__main__":
    auth1 = Authenticator()
    auth2 = Authenticator()

    auth1.login("admin_user")
    auth2.login("moderator_user")

    print("Are both instances identical?:", auth1 is auth2)
    print("Logged in users via auth1:", auth1.get_users())
    print("Logged in users via auth2:", auth2.get_users())