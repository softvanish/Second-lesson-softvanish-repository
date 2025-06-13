# Заповнення списку кубами чисел.

from inspect import isgenerator


def generate_cube_numbers(end):

    x = 2

    while True:

        cube = x ** 3

        if cube > end:
                             # Пока число что генерируется не больше end, этот return игнорируется.
            return
                             # Как только число будет больше end, этот return сработает и функция закончит работу.
        yield cube

        x += 1

##################################


print(list(generate_cube_numbers(1)))

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("OK")
