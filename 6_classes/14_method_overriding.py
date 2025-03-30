class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):  # Constructor overring
        super().__init__()  # Make sure base class init was run too
        self.weigh = 2

    def walk(self):
        print("walk")


mamal = Mammal()
print(mamal.age)
print(mamal.weigh)
