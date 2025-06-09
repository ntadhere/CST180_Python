import unittest
from Dog import Dog
from Cat import Cat
from Bird import Bird
from Kennel import Kennel

class TestAnimalObjects(unittest.TestCase):
    def test_dog_creation(self):
        dog = Dog("Buddy", 3, "Beagle")
        self.assertEqual(str(dog), "Dog: Name: Buddy, Age: 3, Breed: Beagle")

    def test_cat_creation(self):
        cat = Cat("Misty", 2, "Gray")
        self.assertEqual(str(cat), "Cat: Name: Misty, Age: 2, Fur Color: Gray")

    def test_bird_creation(self):
        bird = Bird("Tweety", 1, 15.5)
        self.assertEqual(str(bird), "Bird: Name: Tweety, Age: 1, Wingspan: 15.5 cm")

    def test_kennel_behavior(self):
        dog = Dog("Max", 4, "Labrador")
        kennel = Kennel(dog)
        self.assertEqual(kennel.get_animal_type(), "Dog")