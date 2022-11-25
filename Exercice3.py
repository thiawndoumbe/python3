import turtle
t=turtle.Turtle()
class Square:
    def __init__(self,distance,color):
        self.distance=distance
        self.color=color
    def perimetre(self):
        per= self.distance*4
        return per    
        
    def surface(self):
        surf=self.distance*self.distance
        return surf
    def draw(self):
        t.color(self.color) 
        for i in range(4):
            t.forward(self.distance)
            t.left(90)   
p1=Square(150,"blue")
#p1.perimetre() 
#p1.perimetre()
p1.draw()          