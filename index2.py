# class Person:
#     def bonjour(self):
#         print("bonjour")
#     def aurevoir(self):
#         print("aurevoir")
#     def manger(self,food="orange"):
#         print("je mange",food)    
# p1=Person()
# print(type(p1))
# p1.aurevoir()
# p1.bonjour()
# p1.manger()

# class Person2:
#     def __init__(self,name,age,email):
#         self.name=name
#         self.age= age
#         self.email=email
# p3=Person2("ousmane sonko",48,"oumane@gmail.com")
# print(type(p3))
# print(p3.age)

# class Person3:
#     def __init__(self,name,age,email):
#             self.name=name
#             self.age= age
#             self.email=email
#     def saluer(self,x):
#         print(f"bonjour {x},comment vas tu")
#     #def programmer(self,p="Python"):
        
# # p4=Person3("fatima",21,"fatima99@gmail.com")
# # p4.programmer("java")
# # p4.saluer("amy")
#     def programmer(self,p="Python"):
#         print(f"je m'appelle {self.name} programme en {p}")
#         self.saluer("patrick")
# p4=Person3("Partick",21,"python")
# p4.saluer("patrick")
# p4.programmer("p")


# class Student:
#     def __init__(self,nom,filier,notes):
#         self.nom=nom
#         self.filier=filier
#         self.notes=notes
#     def operation(self):
#         meilleur=max(self.notes)
#         pire=min(self.notes)
#         return (meilleur,pire)
#     def moyen(self):
#         moyen=sum(self.notes/len(self.notes))
#         return moyen

# p1=Student("fatima","info",[12,4,11,18])
# p1.operation("meilleur")


class Student:
    def __init__(self,nom,filier,notes):
        self.nom=nom
        self.filier=filier
        self.notes=notes
    def operation(self,notes):
        maxi = notes[0]
        longueur=len(self.notes)
        for i in range(longueur):
            if self.notes[i] >= maxi:
                maxi = notes[i]
            return maxi
            

    
    
        

    




                   





 







        

            












    














