from Dog import Dog
from Cat import Cat
from Bird import Bird
from Kennel import Kennel

def Main():
    dog = Dog("Charlie", 7, "Golden Retriever")
    cat = Cat("Luna", 5, "Orange Tabby")
    bird = Bird("Kiwi", 2, 25.4)

    kennel1 = Kennel(dog)
    kennel2 = Kennel(cat)
    kennel3 = Kennel(bird)

    print(kennel1)
    print(kennel2)
    print(kennel3)

Main()