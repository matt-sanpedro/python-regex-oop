class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

# Animal is now a derived class
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    # example of overwriting a method
    def eat(self):
        print('I am a dog and I am eating')

mydog = Dog()
print(mydog.who_am_i())
print(mydog.eat())
