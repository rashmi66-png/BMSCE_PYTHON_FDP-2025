class animal:
    def eat(self):
        print("Eating ------")


class Dog(animal):
    def bark(self):
        print("Barking ------")

class Puppy(Dog):
    def cry(self):
        print("crying ------")

a=animal() # object for animal
d=Dog()     #object for Dog
p=Puppy()   #object puppy

a.eat()
d.bark()
d.eat()
p.cry()
p.bark()
p.eat()
