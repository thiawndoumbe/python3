class Distance:
    def __init__(self, number, unit):
        self.number = float(number)
        self.unit = str(unit)
        
    def convert_mètre(self):
        if self.unit =="km":
            resultat = self.number *1000
            return resultat
        elif self.unit =="hm":
            resultat = self.number *100
            return resultat
        elif self.unit =="dam":
            resultat = self.number *10
            return resultat
        elif self.unit =="dm":
            resultat = self.number /10
            return resultat
        elif self.unit =="cm":
            resultat = self.number /100
            return resultat
        elif self.unit =="mm":
            resultat = self.number /1000
            return resultat
        else :
            print("Unité non prise en compte")
    
    def convert(self,new_unit):
        if new_unit== "m":
            return self.convert_mètre()
        elif self.unit == "km":
            result= self.convert_mètre() /1000
            return result
        elif self.unit == "hm":
            return self.convert_mètre() /100
        elif self.unit == "dam":
            return self.convert_mètre() /10
        elif self.unit == "dm":
            return self.convert_mètre() * 10
        elif self.unit == "cm":
            return self.convert_mètre() *100
        elif self.unit == "mm":
            return self.convert_mètre() * 1000
        else:
            print("Unité non prise en compte")

essaie = Distance(20,"dm")
print(essaie.convert_mètre())
print(essaie.convert("m"))
        


