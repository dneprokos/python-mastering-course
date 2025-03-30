class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):  # Bad example of multi-level inheritance because chicken cannot fly
    pass
