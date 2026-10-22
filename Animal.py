from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, legs: int):
        self._legs = legs

    def walk(self):
        print(f"This animal walks on {self._legs} legs.")

    @abstractmethod
    def eat(self):
        pass