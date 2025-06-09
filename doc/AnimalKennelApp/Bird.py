class Bird:
    def __init__(self, name = '', age = 0, wingspan = 0.0):
        self.name = name
        self.age = age
        self.wingspan = wingspan

    def __str__(self):
        return f'Bird: Name: {self.name}, Age: {self.age}, Wingspan: {self.wingspan} cm'
