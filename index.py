# def test(a:float):
#     print(type(a))
    
# test("tyu") 


#permet de forcer l'utilisateur d'entrer des float

class App:
    def __init__(self,a,b):
        if not isinstance(a,float):
            raise ValueError("seulement des float")
p3=App(2.0,5)   

    