#  Генераторна функція

from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):

    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """

    for i in range(end):
        yield begin
        begin = func(begin)


###########################################


test = (some_gen(5, 5, pow))
print(list(test))

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
