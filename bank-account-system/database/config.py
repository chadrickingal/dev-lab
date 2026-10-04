import json
from pathlib import Path

ACCOUNT_FILE = Path(__file__).parent / "accounts.json"

class Database:
    
    def loadAccounts(self):
        with open(ACCOUNT_FILE, "r") as file:
            accounts = json.load(file)
            return accounts

    def addToStorage(self, item):
        with open(ACCOUNT_FILE, "w") as file:
            json.dump(item, file, indent=4)