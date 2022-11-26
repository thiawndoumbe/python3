class Rectangle:
    def __init__(self,long,lar):
        self.long=long
        self.lar=lar
    def perimeter(self):
        per=(self.long+self.lar)*2
        return per
    def surface(self):
        surf= self.long*self.lar 
        return surf
    def draw(self):
        import turtle
        t=turtle.Turtle()
        for i in range(2):
            t.forward(self.long)
            t.left(90)
            t.forward(self.lar)
            t.left(90)
            
p2=Rectangle(150,50)
#p2.perimeter() 
p2.surface()  
p2.draw()                