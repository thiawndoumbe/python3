class Figure:
    def __init__(self,name):
        self.name=name
    def draw(self):
        self.name="#"*10
        i=1
        while i <= len(self.name):
            print(self.name[:i])
            i=i+1
p5=Figure("#")    
p5.draw()