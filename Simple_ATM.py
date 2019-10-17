class BankAccount:
    def __init__(self, name, surname, balance):
        self.name=name
        self.surname=surname
        self.balance=balance
        self.tlist=[]
        print("Hello {0} {1} your balance is: {2}".format(self.name,self.surname,self.balance))
    def add_transaction (self, credit, action):
        if action=='add':
            if credit >0:
                self.balance+=credit
                self.tlist.append({'Action':action,'Credit':credit})
            else:
                print("Bad format")
        elif action=='withdraw' and credit>0:
            if self.balance >= credit:
               self.balance-=credit
               self.tlist.append({'Action': action, 'Credit': credit})
            else:
               print("Not enough funds")
        else:
            print('No such function')
    def current_balance(self):
        print("Your balance is: {}".format(self.balance))
    def show_transactions (self):
        for entry in self.tlist:
            print(entry)
    def is_balance_positive(self):
        if self.balance > 0:
            print('Balance is positive')
            return True
        else:
            print("Balance is negative")
            return False
    @classmethod
    def create_multiple(cls,mname,msurname):
        mlist =[]
        for i in range(len(mname)):
            mlist.append(cls(mname[i],msurname[i],0))
        return mlist


p = BankAccount ('Antis', 'bigxd', 6969)
p.add_transaction(63,'add')
p.current_balance()
p.add_transaction(69, 'withdraw')
p.current_balance()
p.add_transaction(5000000, 'withdraw')
p.add_transaction(-500, 'withdraw')
p.current_balance()
p.add_transaction(5000000, 'add')
p.current_balance()
p.show_transactions()
p.is_balance_positive()
mname=['Antis','Kestas','Tikras']
msurname=('Op','Asd','Asdx')
a = BankAccount.create_multiple(mname, msurname)