from abc import ABC, abstractmethod
class AbstractAnimal:
    @abstractmethod
    def bark(selfself):
        pass


class Dog(AbstractAnimal):
    def bark(self):
        print('Bow Bow')

print(Dog().bark())