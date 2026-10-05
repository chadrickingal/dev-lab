from database.config import Database
from auth.loginAccount import LoginAccount
from auth.createAccount import CreateAccount, DateTimeFromatted
import random 


class BankAccount:
    
    def __init__(self):
        self.__accounts = Database()
        self.__getAccounts = self.__accounts.loadAccounts()
        self.__transactionId = random.randint(10,99)
        self.__dateTime = DateTimeFromatted()
#---------------------------------------------------------------------
# Deposit  
#---------------------------------------------------------------------
    def deposit(self,accountID, amount):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:
                account["balance"] += amount
                transactionHistory = {
                    "id": self.__transactionId,
                    "type": "Deposit",
                    "amount": amount,
                    "date": self.__dateTime.currentDate(),
                }
                account["transactionHistory"].append(transactionHistory)

        self.__accounts.addToStorage(self.__getAccounts)
        return "[Success!]"
#---------------------------------------------------------------------
# Withraw  
#---------------------------------------------------------------------
    def withdraw(self, accountID, amount):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:        

                if amount >= account["balance"] and account["balance"] == 0:
                    return "[Warning!] Insufficient balance. You don't have enough funds for this withdrawal."
                else:
                    account["balance"] -= amount

                    transactionHistory = {
                        "id": self.__transactionId,
                        "type": "Withdraw",
                        "amount": amount,
                        "date": self.__dateTime.currentDate(),
                    }
                    account["transactionHistory"].append(transactionHistory)
                    self.__accounts.addToStorage(self.__getAccounts)
                    return "[Success!] Withdrawal successful."
                    
       
#---------------------------------------------------------------------
# Check Balance 
#---------------------------------------------------------------------
    def Balance(self, accountID):
        for account in self.__getAccounts:
            if accountID == account["accountNumber"]:
                transactionHistory = {
                    "id": self.__transactionId,
                    "type": "Cheking Balance",
                    "date": self.__dateTime.currentDate(),
                }
                account["transactionHistory"].append(transactionHistory)
                self.__accounts.addToStorage(self.__getAccounts)
                return f"{account["balance"]:.2f}"
#---------------------------------------------------------------------
# Transfer
#---------------------------------------------------------------------
    def transfer(self, sendertAccountID, receiverAccountID, amount):
        for senderAccount in self.__getAccounts:
            if sendertAccountID == senderAccount["accountNumber"]:
                for receiverAccount in self.__getAccounts:
                    if receiverAccountID == receiverAccount["accountNumber"]:
                        if amount >= senderAccount["balance"] and senderAccount["balance"] == 0:
                            return "[Warning!] Insufficient balance. You don't have enough funds for this Transfer."
                        else:
                            receiverAccount["balance"] += amount
                            senderAccount["balance"] -= amount
                            
                            senderTransactionHistory = {
                                "id": self.__transactionId,
                                "type": "Transfer",
                                "amount": amount,
                                "reciever": receiverAccount["fullName"],
                                "date": self.__dateTime.currentDate(),
                            }
                            
                            RecievertransactionHistory = {
                                "id": self.__transactionId,
                                "type": "Transfer",
                                "amount": amount,
                                "reciever": senderAccount["fullName"],
                                "date": self.__dateTime.currentDate(),
                            }
                            receiverAccount["transactionHistory"].append(RecievertransactionHistory)
                            senderAccount["transactionHistory"].append(senderTransactionHistory)
                            self.__accounts.addToStorage(self.__getAccounts)
                            return "[Success!] Successfull Transfer"
       
        



bank = BankAccount()
accountLogin = LoginAccount()
accountRegister = CreateAccount()


print(f"Balance: {bank.Balance(3235613311)}")
print(f"Deposit: {bank.deposit(3235613311, 0)}")
print(f"Withdraw: {bank.withdraw(3235613311, 5000)}")
print(f"Transfer: {bank.transfer(3235613311, 2120311405, 5000)}")

# accountRegister.newAccounts("Savings", "Anna34", "annas", "Anna", "Loe", "Santos")

# id = accountLogin.login("juan01","Juan@123")

# # bank.deposit(id, dep)

# bank.transfer(id, 1977845868, 100)
# print(bank.get_Balance(id))

