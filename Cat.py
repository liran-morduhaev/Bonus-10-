from Animal import Animal
from Pet import Pet

class Cat(Animal, Pet):
    def __init__(self, name: str = ""):
        super().__init__(4)
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def play(self):
        print(f"{self._name} is playing with a ball of yarn.")

    def eat(self):
        print(f"{self._name} is eating cat food.")
