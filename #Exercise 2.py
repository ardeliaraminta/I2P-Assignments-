#Exercise 2 
from math import pi 

class Circle:

    def __init__(self, radius = 1.0, colour = "red")
    self.radius = radius
    self.colour = colour 

    def getRadius(self):
        return self.radius = radius 
    
    def setRadius(self,radius):
        self.radius = radius  

    def getColour(self):
        return self.colour

    def setColour(self, colour):
        self.colour = colour 

    def __str__(self):
        return ("The radius of a circle is" + str(self.getRadius()) + "and" + "the colour is " + str(self.getColour()) 
   
    def getArea(self)
        return (pi**2 * self.getRadius())

        
class Cylinder(Circle):

    def __init__(self, height = 1.0, colour = "red"):
        self.height = height 
    
    def getHeight(self):
        return self.height

    def setHeight(self):
        self.height = height 
    
    def __str__(self):
        return ("The radius of a cylinder is" + str(self.getRadius()) + ", the height is" + str(self.getHeight()) + "and the volume of the cylinder is" + str(self.getVolume())

    def getVolume(self):
        return (pi **2 * self.getHeight() * self.getRadius())

    circle = Circle()
    cylinder = Cylinder()

