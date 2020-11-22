from math import pi 

class Circle():

    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
    
    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return ("The radius of a circle is " + str(self.getRadius()) + " and the color of circle is " + self.getColor())
    
    def getArea(self):
        return (pi **2 * self.getRadius())
    

class Cylinder(Circle):

    def __init__(self, height = 1.0, colour = "red"):
        self.__height = height 
    
    def getHeight(self):
        return self.height

    def setHeight(self):
        self.__height = height 
    
    def __str__(self):
        return ("The radius of a cylinder is" + str(self.getRadius()) + ", the height is" + str(self.getHeight()) + "and the volume of the cylinder is" + str(self.getVolume())

    def getVolume(self):
        return (pi **2 * self.getHeight() * self.getRadius())

    circle = Circle()
    cylinder = Cylinder()

