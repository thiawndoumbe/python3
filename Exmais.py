class Domino:
    def __init__(self, valeur_faceA=faceA:0,valeur_faceB="faceB:(0)"):
        self.valeur_faceA=valeur_faceA
        self.valeur_faceB=valeur_faceB
    def affiche(self):
        print(self.valeur_faceA,self.valeur_faceB) 
    def valeur(self):
        somme=self.faceA+self.faceB
        return somme
p1=Domino() 
p1.affiche() 
#p1.valeur()  