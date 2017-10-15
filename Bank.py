class Account:
    def __init__(self, balance):
        self.balance = balance

    def initbalance(self):
        self.balance = 0

    def getbalance(self):
        print("you have", self.balance)

    def deposit(self):
        value = int(input("please input the money you desire to store"))
        self.balance += value
        return "you have",self.balance

    def withdraw(self):
        value = int(input("please input the money you desire to take"))
        if self.balance < value:
            print("The balance isn't enough")
        else:
            self.balance -= value
        return "you have",self.balance,"left"

    def account(self,account):
        self.account=account

class Customers(Account):
    def __init__(self,balance,firstname,lastname,account):
        Account.__init__(self, balance)
        self.firstname = firstname
        self.lastname= lastname
        self.account = account

    def customer(self):
        firstname = input("First name")
        lastname = input("surname")
        accountname = firstname,lastname
        print("Account name:", accountname)

    def getAccount(self):
        return self.account

    def setAccount(self):
        return self.account == self.balance

    def toString(self):
        print("First name:",self.firstname,"Last name:", self.lastname,"Balance:", self.balance, "Bank account number:", self.account)

class Bank():
    def __init__(self,customers,numberofcustomers,bankname):
        self.customers = customers
        self.numberofcustomers = numberofcustomers
        self.bankname=bankname

    def getBankname(self):
        return self.bankname == "CS2021"

    def addcustomer(self):
        firstname = input("please input your first name")
        lastname= input("please input your last name")
        print(firstname,lastname)

    def getnumofcustomers(self):
        print(len(self.numberofcustomers))

    def getCustomer(self):
        nocus = input("please input your customer number")
        print(self.numberofcustomers[nocus])

    def defaultcusval(self):
        self.numberofcustomers = []

numofcus = 0
helloworld = []
defaultuser = Customers(0,"firstname", "lastname", 0)
def main():
    print("Hello what do you want to do?")
    print("[1]Register")
    print("[2]Check Balance")
    print("[3]Deposit/Withdraw")
    print("[4]Check number of total registered user")
    print("[5]Quit")
    b= input("Chosse your choices")
    if b == "1":
        global numofcus
        firstname = input("What is your first name")
        lastname = input("What is your last name")
        defaultuser = Customers(0,firstname,lastname,numofcus)
        helloworld.append(defaultuser)
        numofcus += 1
        hiworld = helloworld[-1]
        hiworld.toString()

        main()
    elif b == "2":
        print("please input your bank account number")
        b=int(input("Your account number"))
        helloworld[b].getbalance()
        main()
    elif b=="3":
        print("please input your bank account number")
        b=int(input("Your account number"))
        helloworld[b].toString()
        print("so what did you want to do?Deposit or Withdraw?")
        choice = input("1/2?")
        if choice == "1":
            helloworld[b].deposit()
            main()
        elif choice =="2":
            helloworld[b].withdraw()
            main()
    elif b=="4":
        print(numofcus)
        main()
    elif b=="5":
        quit()
main()
