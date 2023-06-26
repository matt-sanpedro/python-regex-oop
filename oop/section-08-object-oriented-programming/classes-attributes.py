class Dog():
    # class attributes
    species = 'mammal'

    # self keyword represents the instance of the object itself
    def __init__(self, breed, name, spots):
        # attributes
        # take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # expect boolean True/False
        self.spots = spots
        # attributes do not have parenthesis
        # print(self.species)

    # OPERATIONS/Actions -> Methods
    def bark(self, number):
        print('Woof!  My name is {} and my age is {}'.format(self.name, number))


mysample = Dog(breed='Shih Tzu', name='Fifi', spots=False)
print((mysample.breed, mysample.name, mysample.spots))
# print('Calling method bark: {}'.format(mysample.bark(5)))

class Circle():

    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius ** 2 * Circle.pi

    # method
    def get_circumference(self):
        return self.radius * Circle.pi * 2
    

mycircle = Circle(5)