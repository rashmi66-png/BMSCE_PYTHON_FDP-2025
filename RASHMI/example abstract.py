from abc import ABC, abstractmethod

class ANIMAL(ABC):

    @abstractmethod
    def eat(self):
        pass

class Dog(ANIMAL):
    def eat(self):
        print('Dog is eating')

c=Dog()
c.eat()
