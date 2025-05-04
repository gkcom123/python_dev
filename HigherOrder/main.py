def square(x):
    return x * x


def apply_function(func, numbers):
    return [func(num) for num in numbers]


numbers = [1, 2, 3, 4]
result = apply_function(square, numbers)
print(result)

