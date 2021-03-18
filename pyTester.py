from random import seed, randint


class PyTester:

    def print_function(self, args, fun):
        for x in args:
            print('f(', x, ')=', fun(x), sep='')

# List comprehensions versus generators
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

# Lambda functions
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

ptester = PyTester()
ptester.print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

# map function utilization
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# filter function utilization
seed()
data = [randint(-10, 10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)