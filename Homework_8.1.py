# Додати 1 до числа

def add_one(some_list):
    number = ""
    result = []
    last_result = []

    for i in some_list:
        number += str(i)          # Превращаем числа в строку

    int_number = int(number)
    number_1 = int_number + 1     # Превращаем в число и добавляем один

    number_1 = str(number_1)      # Назад в строку

    for num in number_1:
        num = int(num)
        last_result.append(num)   # Снова в число и добавляем в список

    print(last_result)
    return last_result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
