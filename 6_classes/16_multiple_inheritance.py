class Employee:
    def greet(self):
        print("Employee Greet")


class Person():
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # Also bad example. First base class greet will be used
    pass


manager = Manager()
print(manager.greet())  # Employee Greet


# Good example of multiple inheritance is to create abstract classes without common things
class Flyer:
    def fly(self):
        print("fly")


class Swimmer:
    def swim(self):
        print("swim")


class FlyingFish(Flyer, Swimmer):
    pass
