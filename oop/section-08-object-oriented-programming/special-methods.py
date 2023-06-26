'''
SPECIAL METHODS
Also called magic/dunder methods 
'''
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    # method below is invoked when object is deleted
    def __del__(self):
        print('A book object has been deleted')


b = Book('Python Rocks', 'Monty', 111)

# accessing the values
print(b)
print(str(b))
print(len(b))

# to delete the instance from memory
del b
# print(b) # raises NameError
