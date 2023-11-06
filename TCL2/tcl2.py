class BankAccount:
    def __init__(self, accountNum, initailBalance):
        self.accountNum = accountNum
        self.balance = initailBalance

    def deposit(self, balance): # 입금
        self.balance += balance
    
    def withdraw(self, balance): # 출금
        if self.balance < balance:
            print("잔액 부족")
        else :
            self.balance -= balance
    
    def get_balance(self):
        return self.balance

account1 = BankAccount("12345", 10000)
account1.deposit(500)
account1.withdraw(200)
print(f"계좌 1의 현재 잔액: {account1.get_balance()}원 ")
