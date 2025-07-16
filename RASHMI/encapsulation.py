class bankaccount:
    def __init__(self,name,balance, pin):
        self.name=name
        self._balance=balance #protected
        self.__pin=pin   #cant be accesible.private not even objects can access it


    def showbalance(self):
        print(f"account holder: {self.name}")
        print(f"account balance: {self._balance}")
        print(f"pin: {self.__pin}")

acc=bankaccount("Rashmi",100,"12345")

print(acc.name)
print(acc._balance)
print(acc.__pin)
