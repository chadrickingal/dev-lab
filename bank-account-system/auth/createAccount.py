import random
from database.config import Database
from datetime import datetime

class DateTimeFromatted:

    # Get a Date and Time Realtime and formatted
    @staticmethod
    def currentDate():
        return datetime.now().strftime("%B %d, %Y")

    @staticmethod
    def currentTime():
        return datetime.now().strftime("%H:%M:%S %p")

    
class CreateAccount:
    def __init__(self):
        self.storage = Database()
        self.accounts = self.storage.loadAccounts()

    def newAccounts(self,accountType, username, password, firstName,lastName, middleName=" ", extraName=" "):
        accountNumber = random.randint(1000000000, 9999999999)
        newAccount = {
            "accountNumber": accountNumber,
            "fullName": {
                "firstName": firstName,
                "middleName": middleName,
                "lastName": lastName,
                "extraName": extraName
            },
            "accountType": accountType,
            "username": username,
            "password": password,
            "createdAt":{
                "time": DateTimeFromatted.currentTime(),
                "date": DateTimeFromatted.currentDate()
            },
            "transactionHistory": [],
            "balance": 0
        }
        self.accounts.append(newAccount)

        self.storage.addToStorage(self.accounts)

    def forgotPassword(self):
        pass