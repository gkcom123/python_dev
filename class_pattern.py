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
        return "woof"
class Cat:
    def speak(self):
        return "meao"
def animal_factory(animal= 'dog'):
    if animal =='Dog': return Dog()
    if animal =='Cat': return Cat()

pet = animal_factory("Dog")
print(pet.speak())

# Builder pattern
class PizzaBuilder:
    def __init__(self):
        self.pizza = []
    def add_cheese(self):
        self.pizza.append("cheese")
        return self
    def add_pepporini(self):
        self.pizza.append("peporini")
        return self
    def build(self):
        return self.pizza
pizza = PizzaBuilder().add_cheese().add_pepporini().build()
print(pizza)


class PayByCard:
    def pay(self, amount): print(f"Paying {amount} by card")

class PayByCash:
    def pay(self, amount): print(f"Paying {amount} by cash")

class PaymentProcessor:
    def __init__(self, strategy): self.strategy = strategy
    def pay(self, amount): self.strategy.pay(amount)

payment = PaymentProcessor(PayByCash())
payment.pay(100)


def make_bold(func):
    def wrapper(): return "<b>" + func() + "</b>"
    return wrapper

@make_bold
def greet(): return "Hello"

print(greet())  # <b>Hello</b>


# Decorator pattern
def make_bold(func):
    def wrapper(): return "<b>" + func() + "</b>"
    return wrapper

@make_bold
def greet():
    return "Hello"

print(greet())


class Subject:
    def __init__(self): self.observers = []
    def register(self, observer): self.observers.append(observer)
    def notify_all(self, data):
        for observer in self.observers:
            observer.update(data)

class Observer:
    def update(self, data): print(f"Received: {data}")

s = Subject()
s.register(Observer())
s.notify_all("New event!")
