# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:46:51 2022

@author: Precision 7510
"""
"""
Time=open("D:\\L1python\\L1python\\fiche.txt")
l=Time.readline()
print(l)
l=Time.splitlines
listes=[]
for i in l:
    l.append(listes)
""" 
"""

Time=open("C:\\Users\\Precision 7510\\Desktop\\Python3\\fiches.txt")
line=Time.read()
lin=Time.readlines()
chaine=[]
for i in lin:
    lin.splitelines()
    print(lin)
    lin.append(chaine)
for i in chaine:
    m=chaine[2]
    t=chaine[3]
    imc=(m*t**2)
    print(imc)    

"""
       
""" masse = int(input("Entrez votre poids en kg:"))
taille = float(input("Entrez votre taille en m"))
def imc(masse,taille):
    return masse/(taille**2)
imc = float
if imc>25.0:
    print("Vous êtes en surpoids.")
elif imc<18.5:
    print("Voues êtes trop maigre.")
else:
    print("Vous avez une corpulence normale.")"""
# def calcul_imc(masse,taille):
#     Time = open("C:\\Users\\Precision 7510\\Desktop\\Python3\\fiches.txt")
#     line=Time.read()
#     lin=Time.readlines()
#     chaine=[]
#     for i in lin:
#         lin.splitelines()
#         print(lin)
#         lin.append(chaine)
#     for i in chaine:
#         nom=i[0]
#         prenom=i[1]
#         m=int(i[2])
#         t=float(i[3])
#         imc=(m*t**2)
#         print(imc) 
# t=calcul_imc(12,1.55)  
# print(t)    




# def imc(o):
#     #o=openUsers("C:\\Users\\Precision 7510\\Desktop\\Python3")
#     file_content=o.read()
#     lines=file_content.splitlines()
#     print(lines)
#     lst=[]
#     for line in lines:
#         #print(line.split())
#         lst.append(line.split())
#         #print(lst)
#     for i in lst:
#         #patient=i[0] +

def copieFichier(source, destination):
    "copie intégrale d'un fichier" 
    fs = open(source, 'r')
    fd = open(destination, 'w')
    while 1:
        txt = fs.read(50)
        if txt =="":
            break
        fd.write(txt)
    fs.close()
    fd.close()
    return








    
    
    
    
    
    
    
    
    
    