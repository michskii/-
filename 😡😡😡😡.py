from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def habitat(self):
        pass
class lion(Animal):
        def sound(self):
            return "roar"
        def habitat(self):
            return "lives in Savannah"
    
class penguin(Animal):
        def sound(self):
            return "honk"
        def habitat(self):
            return "lives in icy regions"
def wild_animal_sanctuary():
    animals=[lion(),penguin()]
    for animal in animals:
        print(f"{animal.__class__.__name__}:")
        print(f"sound:{animal.sound()}")
        print(f"habitat:{animal.habitat()}")
wild_animal_sanctuary()