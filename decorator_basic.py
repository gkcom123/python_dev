def decorator_function(original_function):
    def wrapper_function():
        print(f"Warpper executed before {original_function.__name__}")
        return original_function()

    return wrapper_function


@decorator_function
def hello():
    print("Hello World : Demo of Decorator function")


hello()


def decorator_function_add(original_function):
    def wrapper_function(*args, **kwargs):  # ✅ Accepts any number of arguments
        print(f"Wrapper executed before {original_function.__name__} {args} {kwargs}")
        return original_function(*args, **kwargs)  # ✅ Pass arguments correctly

    return wrapper_function


@decorator_function_add
def add(a, b):
    return a + b


print(add(3, 5))  # ✅ Works correctly


def logging_decorator(original_function):
    def log_me(*args):
        print(f"You called {original_function.__name__} {args}")
        res = original_function(*args)
        print(f"It returned: {res}")

    return log_me


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)

data = [1, 1, 0, 1, 0, 2, 3, 2]

res = sorted(data)
print(res)
