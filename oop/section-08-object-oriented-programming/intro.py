class Dog():
    # self keyword represents the instance of the object itself
    def __init__(self, breed, name, spots):
        # attributes
        # take in the argument
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # expect boolean True/False
        self.spots = spots

mysample = Dog(breed='Shih Tzu', name='Fifi', spots=False)

print((mysample.breed, mysample.name, mysample.spots))
