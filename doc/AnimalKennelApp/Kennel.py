class Kennel:
    def __init__(self, animal=None):
        self.animal = animal

    def get_animal_type(self):
        return type(self.animal).__name__

    def __str__(self):
        return f'Kennel Animal: {self.animal}'