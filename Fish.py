from Animal import Animal
from Pet import Pet

class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self._name = ""

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def play(self):
        print(f"Fish {self._name} swims playfully.")

    def walk(self):
        print("Fish can't walk, they swim!")

    def eat(self):
        print("Fish eats algae and fish flakes.")