from abc import ABC, abstractmethod

class AbstractRecipe(ABC):

    def execute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


class Recipe1(AbstractRecipe):

    def prepare(self):
        print('Do the dishes')
        print('Get raw materials')

    def recipe(self):
        print('Execute the steps')

    def cleanup(self): pass


class MicrowaveRecipe(AbstractRecipe):

    def prepare(self):
        print('Do the dishes')
        print('Get raw materials')
        print('Switch on microwave')

    def recipe(self):
        print('Execute the steps')

    def cleanup(self):
        print('Switch off microwave')


Recipe1().execute()
print()
MicrowaveRecipe().execute()

# prepare - raw materials
# recipe
# cleanup