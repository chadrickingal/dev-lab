from database.config import Database

class LoginAccount:
    def __init__(self):
        self.__storage = Database()
        self.__accounts = self.__storage.loadAccounts()


    def login(self, username, password):
        for account in self.__accounts:
            if account["username"] == username:
                if account["password"] == password:
                    return account["accountNumber"]
            print("[Incorrect!] Incorrect password")  
        print("[Incorrect!] Incorrect username")          




