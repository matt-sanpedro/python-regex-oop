'''
POLYMORPHISM
In Python, refers to the way object classes can share same method name.

Methods can be called from the same place.
'''

class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
    


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

# up to the class to see what opens 
for pet in [niko, felix]:
    print(type(pet))
    property(pet.speak())

def pet_speak(pet):
    print(pet.speak())

class Animal():

    def __init__(self, name):
        self.name = name

    # this method is expected to be created with each inheritance
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

# myanimal = Animal('Fred')
# myanimal.speak()



class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'
    

class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
pet_speak(fido)
