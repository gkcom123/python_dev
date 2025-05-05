import timeit
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Calling static methods using the class
print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.multiply(5, 3))  # Output: 15

# Calling static methods using an instance
math = MathOperations()
print(math.add(10, 20))  # Output: 30


print(timeit.timeit("(1, 2, 3, 4, 5)", number=1000000))  # Tuple
print(timeit.timeit("[1, 2, 3, 4, 5]", number=1000000))  # List