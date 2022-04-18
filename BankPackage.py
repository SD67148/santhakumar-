class BankInfo:
    class Account:
        balance=0
        l=[]
        def __init__(self,amount,name):
            self.amount=amount
            self.name=name

        def Deposit(self,amount):
            self.balance+=amount

        def Withdrawal(self,amount):
            self.balance-=amount

        def __eq__(self,other):
            if (isinstance(other,BankInfo.Account)):
                return self.balance==other.balance
            return False
        def __ne__(self,other):
            return self.balance !=other.balance
        def __le__(self,other):
            return self.balance<=other.balance
        def __ge__(self,other):
            return self.balance>=other.balance
        def __lt__(self,other):
            return self.balance<other.balance
        def __gt__(self,other):
            return self.balance>other.balance
        '''
        def AddNominee(self,nominee):
            self.Nominee=l.append(nominee)
        def __cal__(selfself):
            return self.Nominee'''


