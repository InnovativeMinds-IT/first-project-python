class Account:
    print('\tWelcome to YBank')
    print("     ----------------------------------------")
    def __init__(self,accbal):
        if accbal<0.0:
            print("invalid balance")
            accbal=0.0
        self.accbal=accbal
    def credit(self,camt):
        if camt<0.0:
            print("please enter valid amt")
        else:
            self.accbal=self.accbal+camt
        print("Current balance after credit",self.accbal)
    def debit(self,damt):
        if damt> self.accbal:
            print("debit amount exceeded account balance")
        else:    
            self.accbal=self.accbal-damt
            print("current balance after debit",self.accbal)
    def getBalance(self):
        print("curent balance is",self.accbal)
        
class SavingAccounts(Account):
    time=12
    def __init__(self,accbal,roi):
        self.roi=roi
        super().__init__(accbal)
    def calculateInterest(self):
        i=self.accbal*SavingAccounts.time*self.roi*0.01
        print("interest rate is",i)

class CheckingAccount(Account):
    def __init__(self,accbal,fee):
        self.fee=25
        super().__init__(accbal)
    def credit(self,camt):
        self.camt=camt
        if camt<=0.0:
            print("please enter valid amt")
        else: 
            self.accbal=self.accbal+self.camt-self.fee
            print("Balance after credit with charges",self.accbal)
    def debit(self,damt):
        self.damt=damt
        if damt>=self.accbal:
            print("debit amount doesn't exceed the account balance")
        else:
            self.accbal=self.accbal-self.damt-self.fee
            print("current balance after debit with charge",self.accbal)
class CurrentAccount(Account):
    def __init__(self,accbal,maxlimit):
        self.maxlimit=maxlimit
        super().__init__(accbal)
    def debit(self,damt):
        if self.accbal<=0.0:
            self.accbal=range(0,self.maxlimit)
        else:
            print("this is not available for you")
            
t1=SavingAccounts(50000,7.89)
t2=CheckingAccount(50000,25)
t3=CurrentAccount(0,75000)
t1.credit(23000)
t1.debit(23000)
t1.calculateInterest()
t2.credit(0)
t2.debit(49000)
t3.debit(-554)

            
        



        
            
        
