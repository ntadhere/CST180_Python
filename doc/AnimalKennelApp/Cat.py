class Cat:
    def __init__(self, name = '', age = 0, fur_color = ''):
        self.name = name
        self.age = age
        self.fur_color = fur_color

    def __str__(self):
        return f'Cat: Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color}'
