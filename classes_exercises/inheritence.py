class Animal():
    #This is our base class
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):
    #This is our derived class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        print("I am a dog")
    
    def bark(self):
        print("WOOF")
        
myDog = Dog()
myDog.who_am_i()