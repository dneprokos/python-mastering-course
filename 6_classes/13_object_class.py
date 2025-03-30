class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


mamal = Mammal()
print(isinstance(mamal, Mammal))  # True
print(isinstance(mamal, Animal))  # True
print(isinstance(mamal, object))  # True

print(issubclass(Mammal, Animal))  # True
print(issubclass(Mammal, object))  # True

o = object()  # base object class all classes based on
