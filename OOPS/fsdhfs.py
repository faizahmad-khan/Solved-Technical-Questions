#Encapsulation
class bankAccount:
   def __init__(self,owner,balance):
     self.owner = owner
     self.__balance = balance

     def deposit(self,amount):
        self.__balance +=amount
     def get_balance(self):
        return self.__balance


     acc = bankAccount(owner:"faiz", balance:10000)   