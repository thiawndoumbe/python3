class BankAccount:
    def __init__(self,name="",number=0,amount=0):
        self.name=str(name)
        self.number=float(number)
        self.amount=float(amount)
    def deposit(self):  
        montant=int(input("combien veux tu verse:"))
        self.amount=self.amount+montant
        print("depot fait avec succe")
    def withdraw(self):
        montant=float(int(input("combien veux tu retirer :")))
        if montant>self.amount:
            print("insuffisant")
        else:
            self.amount=self.amount-montant
p2=BankAccount()
print(p2.deposit())
print(p2.withdraw())            
              
        
        