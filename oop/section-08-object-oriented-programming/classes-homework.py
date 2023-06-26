from math import pi

# PROBLEM 1: Line Computation
class Line:
    
    def __init__(self,coor1,coor2):
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]
    
    def distance(self):
        # formula: d = sqrt( (x2-x1)^2 + (y2-y1)^2 )
        return ( (self.x2 - self.x1)**2 + (self.y2 - self.y1)**2 ) ** (1/2)
    
    def slope(self):
        # formula: m = (y2 - y1)/(x2 - x1)
        return (self.y2 - self.y1) / (self.x2 - self.x1)


# PROBLEM 1: example output
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

# print(f"Imported pi: {pi}")

# PROBLEM 2: Cylinder Computation
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.pi = pi
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return (2 * self.pi * self.radius) * (self.height + self.radius)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
