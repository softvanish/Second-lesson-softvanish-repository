#Знайти суму елементів із парними індексами

lst = [0, 1, 2, 3, 4, 5]

numbers = [lst[i] for i in range(0, 5, 2)]                                       # Делаем самое главное
print(f"Your new list: {numbers}")
result = (numbers[0] + numbers[1] + numbers[2]) * lst[-1]                        # Считаем
print(f"If you add them all and multiply \non 'lst[-1]' you will get: {result}")
