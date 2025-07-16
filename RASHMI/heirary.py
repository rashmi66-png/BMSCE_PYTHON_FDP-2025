class animal:
    def eat(self):
        print("Eating ammmmmmm------")


class Dog(animal):
    def bark(self):
        print("Barking bowwwwwwwwww------")

class cat(animal):
    def meow(self):
        print("meow meowwwwwwwww ------")

a=animal() # object for animal
d=Dog()     #object for Dog
c=cat()   #object puppy

a.eat()
d.eat()
d.bark()
c.eat()
c.meow()
