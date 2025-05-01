class Person:
    # Class variable
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))


# Calling class method using the class
print(Person.get_population())  # Output: 0

# Creating an instance using the class method
person1 = Person.from_string("Alice-30")
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30
print(Person.get_population())  # Output: 1
