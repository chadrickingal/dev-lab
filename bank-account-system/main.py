from database.config import Database
from auth.loginAccount import LoginAccount
from auth.createAccount import CreateAccount

class BankAccount:
    def __init__(self):
        self.__accounts = Database()
        self.__getAccounts = self.__accounts.loadAccounts()
#---------------------------------------------------------------------
# Deposit  
#---------------------------------------------------------------------
    def deposit(self,accountID, deposit):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:
                account["balance"] += deposit
        self.__accounts.addToStorage(self.__getAccounts)
#---------------------------------------------------------------------
# Withraw  
#---------------------------------------------------------------------
    def withraw(self, accountID, withdraw):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:         
                if withdraw >= account["balance"]:
                    print("[Warning!] Insufficient balance. You don't have enough funds for this withdrawal.")
                else:
                    account["balance"] -= withdraw
                    print("[Success!] Withdrawal successful.")
                    break
        self.__accounts.addToStorage(self.__getAccounts)
#---------------------------------------------------------------------
# Check Balance 
#---------------------------------------------------------------------
    def get_Balance(self, accountID):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:
                return f"{account["balance"]:.2f}"
#---------------------------------------------------------------------
# Transfer
#---------------------------------------------------------------------
    def transfer(self, sendertAccountID, receiverAccountID, ammount):
        for senderAccount in self.__getAccounts:
            if sendertAccountID == senderAccount["accountNumber"]:
                for receiverAccount in self.__getAccounts:
                    if receiverAccountID == receiverAccount["accountNumber"]: 
                            receiverAccount["balance"] += ammount
                            senderAccount["balance"] -= ammount
                            print("[Successfull!] Successfull Transfer")
        self.__accounts.addToStorage(self.__getAccounts)
bank = BankAccount()
accountLogin = LoginAccount()
accountRegister = CreateAccount()

accountRegister.newAccounts("Checking", "juan01", "Juan@123", "Juan", "Dela Cruz", "Santos", "Jr.")

id = accountLogin.login("juan01","Juan@123")

# bank.deposit(id, dep)

bank.transfer(id, 1977845868, 100)
print(bank.get_Balance(id))

