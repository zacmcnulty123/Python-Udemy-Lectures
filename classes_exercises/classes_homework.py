#Problem 1
class Line:
    def __init__(self, coor1, coor2):
        self.line = (coor1, coor2)
    
    def distance(self):
        return ((self.line[1][0] - self.line[0][0])**2 \
                + (self.line[1][1] - self.line[0][1])**2)**0.5

    def slope(self):
        return (self.line[1][1] - self.line[0][1]) \
               / (self.line[1][0] - self.line[0][0]) 

coordinate1 = (3,2)
coordiante2 = (8,10)

li = Line(coordinate1, coordiante2)
print(li.distance())
print(li.slope())

#Problem 2
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14
    
    def volume(self):
        return self.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return (2 * self.pi * self.radius * self.height)  \
                + (2 * self.pi * self.radius**2) 

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())