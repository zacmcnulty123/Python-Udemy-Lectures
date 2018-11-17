class Circle():
    
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = radius**2 * Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)

print(my_circle.get_circumference())
print(my_circle.area)