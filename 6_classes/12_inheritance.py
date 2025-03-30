class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub-class


class Mammal(Animal):
    def walk(self):
        print("walk")

# Animal: Parent, Base
# Fish: Child, Sub-class


class Fish(Animal):
    def swim(self):
        print("swim")


mamal = Mammal()
print(mamal.eat())  # eat
print(mamal.walk())  # walk
print(mamal.age)  # 1

fish = Fish()
print(fish.eat())  # eat
print(fish.swim())  # swim
print(fish.age)  # 1
