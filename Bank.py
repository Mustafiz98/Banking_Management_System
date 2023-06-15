
class Person:
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password

class Bank:
    __total_balance = 4000
    __total_loan_amount = 0

    __user_balance = {}
    __user_info = []
    __switch_loan = True
    
    def switch_loans(self, val):
        Bank.__switch_loan = val
    #----------------------------------------------------------------------------  
    def Creat_account(self, name, password):
        new_user = Person(name, password)
        self.__user_info.append(vars(new_user))
        
        self.__user_balance[name] = 0

    def Get_user(self, name, password):
        flag = 1
        for user in self.__user_info:
            if name == user['name'] and password == user['password']:
                flag = 0
                return True
        if flag:
            return False
    #----------------------------------------------------------------------------  
    
    @property
    def Get_balence(self):
        return self.__total_balance
    
    @property
    def Get_loan_amount(self):
        return self.__total_loan_amount
    
    def deposit(self, user, amount): # ---------- deposit money -----------------
        self.__user_balance[user] += amount
        Bank.__total_balance += amount
        print(f"{'-'*25}\nYour deposit {amount} done!")
    
    def withdrawal(self, user, amount): # ------- withdrawal money --------------
        print('-'*25)
        if amount <= self.__user_balance[user]: 
            if self.__total_balance < amount :
                print("The bank is bankrupt. ")
            else:  
                self.__user_balance[user] -= amount
                Bank.__total_balance -= amount
                print("your withdrawal done! ")
                print(f"Amount: {amount} \nCurrent Balance: {self.__user_balance[user]}")
        else:
            print(f"Not enough money!")
    
    def check_user_balance(self, user): # ---------- balance check ----------------
        return self.__user_balance[user]

    def money_transfer(self, sender, receiver, amount): # --- money transfer -------
        flag = 0
        for user in self.__user_info:
            if sender == user['name']:
                if self.__user_balance[sender] >= amount:
                    self.__user_balance[sender] -= amount
                    flag = 1
                else :
                    print("Not enough money ")
                    return False         
        if flag:
            for user in self.__user_info:
                if receiver == user['name']:
                    self.__user_balance[receiver] += amount
                    print(f"Money Transfer to: {receiver} successful")
                    print(f"Amount: {amount}, Current balance: {self.__user_balance[sender]}")
                    return True
        else :
            print("Account does not match")
            return False     
                    
    def give_loan(self, borrower, amount): # ----------- giving loan --------------
        print('-'*25)
        flag = 1
        if self.__switch_loan == True :
            for user in self.__user_info:
                if borrower == user['name']:
                    flag=0
                    if (self.__user_balance[borrower]*2) >= amount <= Bank.__total_balance :
                        self.__user_balance[borrower] += amount
                        Bank.__total_balance -= amount
                        Bank.__total_loan_amount += amount
                        
                        print(f"You got a loan tk. {amount}")
                    else:
                        print("Amount is very large")                       
            if flag:
                print("account not match")
        else :
            print("loan option is off ")

class User(Person): # ------------------ user class -------------------------------
    bank = Bank()
    transaction_histores = {}
    def __init__(self, name, password) -> None:
        if self.bank.Get_user(name,password) == False:
            print(f"{'-'*30}\n{name}'s Account does not match")
        super().__init__(name, password)

        self.transaction_histores[self.name] = []

    def deposit(self, amount):
        self.bank.deposit(self.name, amount)
    
    def withdrawal(self, amount):
        self.bank.withdrawal(self.name, amount)

    def check_balance(self):
        print(f"{'-'*25}\nYour total balance: {self.bank.check_user_balance(self.name)}")

    def money_transfer(self, receiver_name, amount):
        print('-'*37)
        flag = self.bank.money_transfer(self.name , receiver_name, amount)
        if flag:
            self.transaction_histores[self.name].append(f"Receiver: {receiver_name} , Amount: {amount}")
        
    def  transaction_history(self):
        print(f"-------- {self.name}'s Txn --------")
        for value in self.transaction_histores[self.name]:
            print(value)

    def take_loan(self, amount):
        self.bank.give_loan(self.name, amount)

class Admin(Person): # -------------------------- admin class ----------------------
    def __init__(self, name, password) -> None:
        super().__init__(name, password)

    bank = Bank()
    
    def total_bank_balance(self):
        print(f"{'-'*25}\nTOTAL BANK BALANCE: {self.bank.Get_balence}")

    def total_loan_amount(self):
        print(f"{'-'*25}\nTOTAL LOAN AMOUNT: {self.bank.Get_loan_amount}")

    def switch_loan_feature(self, switch):
        self.bank.switch_loans(switch)


Abc_bank = Bank()

Abc_bank.Creat_account('Admin',123)
admin = Admin('Admin', 123)

Abc_bank.Creat_account('Mahmud', 246)
Abc_bank.Creat_account('Rafsan', 135)
Abc_bank.Creat_account('Shahid', 468)

user_1 = User('Mahmud', 246)
user_2 = User('Rafsan', 135)
user_3 = User('Shahid', 468)
user_4 = User('Asif', 135) # There is no 'Created Account' as named 'Asif' here.

admin.total_bank_balance()
print()

user_1.deposit(1000)
user_1.check_balance()
user_1.take_loan(2000)
user_1.money_transfer('Rafsan', 1200)
print()

user_2.check_balance()
user_2.withdrawal(200)
print()

user_1.money_transfer('Shahid', 800)
user_1.transaction_history()
print()

admin.switch_loan_feature(False)
user_3.take_loan(1500)
admin.switch_loan_feature(True)

admin.total_bank_balance()
print()

user_1.check_balance()
user_2.check_balance()
user_3.check_balance()
print()

user_2.take_loan(2000)
user_3.take_loan(800)
print()

user_1.withdrawal(500)

admin.total_bank_balance()
admin.total_loan_amount()


print('-'*25)