def count_in_loop(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_in_loop(5):
    print(num)


def my_decorator(gen_func):
    def wrapper(*args, **kwargs):
        print("Generator started")
        yield from gen_func(*args, **kwargs)
        print("Generator finished")

    return wrapper


@my_decorator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


for num in countdown(3):
    print(num)
