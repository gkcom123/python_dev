class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)


class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meao"


def Animal_Factory(animal="dog"):
    if animal == 'dog':
        return Dog()
    elif animal == 'cat':
        return Cat()


pet = Animal_Factory("cat")
print(pet.speak())


class PizzaBuilder:
    def __init__(self):
        self.pizza = []

    def add_cheese(self):
        self.pizza.append("Cheese")
        return self

    def add_peporoni(self):
        self.pizza.append("peproni")
        return self

    def build(self):
        return self.pizza


pizza = PizzaBuilder().add_peporoni().add_cheese().build()
# pizza.add_peporoni().add_cheese().build()
print(pizza)
