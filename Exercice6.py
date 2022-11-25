class Calculor:
    def __init__(self,a,b):
        self.a=float(a)
        self.b=float(b)
    def add(self):
        addition=self.a+self.b
        return addition
    def substract(self):
        sous=self.a-self.b
        return sous
    def  multiply(self):
        mult=self.a*self.b
        return mult
    def divide(self):
        if self.b!=0:
            div=self.a/self.b
            return div 
        else:
            print("division impossible")
    def power(self):
        pow=self.a**self.b
        return pow
p6=Calculor(12,2)  
# p6.add()   
# p6.substract()      
# p6.multiply()            
p6.divide()
p6.power()