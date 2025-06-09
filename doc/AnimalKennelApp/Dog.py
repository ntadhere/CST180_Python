class Dog:
    def __init__(self, name = '', age = 0, breed = ''):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'Dog: Name: {self.name}, Age: {self.age}, Breed: {self.breed}'
