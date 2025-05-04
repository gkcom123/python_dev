def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


def multiplier_way(number, factor):
    return number * factor


double = multiplier(2)
print(double(2))
result = double(5)
print(result)

print(multiplier_way(2, 3))

# using maps
nums = [1, 2, 34, 2]
squared = map(lambda x: x ** 2, nums)
print(list(squared))  # Output: [1, 4, 9, 16]

x = 10
print(type(x))
x = True
print(type(x))

