# Генератор простих чисел.

from inspect import isgenerator


def prime_generator(end):

    x = 2
    integer = True

    while True:

        if x <= end:

            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    integer = False
                    break
                else:
                    integer = True

            if integer:
                yield x

        else:
            break

        x += 1


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'

assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'

print('Ok')
