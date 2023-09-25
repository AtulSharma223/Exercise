class Bank:
    def __init__(self):
        self.account={}
    def create_account(self,account_number,balance):
        if account_number in self.account:
            print("Account number exists")
        else:
            self.account[account_number]=balance
            print("Account Successfully created")
    def add_blance(self,account_number,amount):
        if(account_number in self.account):
            self.account[account_number]+=amount
            print("Transicition successful")
        else:
            print("No Acoount found")
    def withdraw(self,account_number,amount):
        if(account_number in self.account):
            if(self.account[account_number]<amount):
                print("Insufficient balance")
            else:
                self.account[account_number]-=amount
                print("Transicition successful")
        else:
            print("No account found")


customer1=Bank()
customer1.create_account(101,2000)
customer2=Bank()
customer2.create_account(102,1000)

customer1.add_blance(101,10000)
customer2.withdraw(102,3000)
