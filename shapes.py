# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr
from inspect import classify_class_attrs
import math

class Circle:
 def __init__(self,radius):
     self.radius=radius
 def area(self):
     A=math.pi*self.radius*self.radius
     return f"The area of the circle is {A}"
 def circumference(self):
     B=2*math.pi*self.radius
     return f"The circumference of the circle is {B}"


# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        A=self.side**2
        return f"The area of the square is {A} "
    def perimeter(self):
        p=self.side*4
# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w) 
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):
        A=self.l*self.w
    def perimeter(self):
        B=2(self.l+self.w)
# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
class Sphere:
    def __init__(self,r):
        self.r=r
    def surface_area(self):
        A=4(math.pi*self.r**2)
        return f"The surface area of a sphere is{A}"
    def volume(self):
        B=4/3(math.pi*self.r**2)
        return f"The volume of a sphere is {B}"

        

    

    