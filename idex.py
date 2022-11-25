# heritage simple
# class Voiture:
#     def __init__(self, wheels,max_speed,cylindre) :
#         self.wheels=wheels
#         self.max_speed=max_speed
#         self.cylindre=cylindre
#     def demarrer(self):
#         pass
        
#     def arreter (self): 
#         pass
# class Moto(Voiture):...
# m1=Moto(2,150,300)
# print(m1.max)   
# print(m1.cylindre) 
# class Camion (Voiture):
#     pass  
# class A :
#     def __init__(self,calculer):
#         self.calculer=calculer
        
# class B(A):...
#     def __init__(self;poids) -> None:
#         pass
    
    
# class C(B):
#     pass
# class D(C):
#     pass
    
#      #heritage + quelque chose    
# class Car :
#     def drive(self):
#         return "I'am driving"
# class Superclas(Car):
#     def autodrive(self):
#         return "self.driving,atodive"
# v1=Superclas()
# v1.drive  

# # heritage+ajout d"attribut dans la class fille ajouter une nouvelle contructeur
# class Person:
#     def __init__(self,name) -> None:
#         self.name=name
# class Student(Person):
#     def __init__(self, name,email,address):
#         super().__init__(name) #initialisateur de la class mer merci d'initialiser l'attribut name
#         self.email=email
#         self.address=address
# s1=Student("thiaw","thiawnd99@gmail.com","fann")
# print(s1.name,s1.email,s1.address)           
     #super()   
class Person1:
    def __init__(self,firsname,lasname,age) -> None:
        self.name=firsname
        self.lasname=lasname
        self.age=age
class Student(Person1):
    def __init__(self,firsname,lasname,age,email):
        super().__init__(firsname,lasname,age)
        self.email=email
a=Student("thiao","ndoumbe",23,"nd@99")  
print(a.age,a.name,a.lasname,a.email)      
#surchage redefinir une methode qui v
class P:
    def dirbonjour(self):
        return "bonjour"
class M(P):...

    def bonjour(self):
        return "salut"

    
    
        
                            
                                                        