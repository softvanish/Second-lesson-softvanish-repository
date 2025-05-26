#Конвертер із числа в дату

while True:

    number = int(input("Enter number your number: "))

    if number > 8640000:

        print("This number is too big. Max value - 8640000.")

        continue
    else:
        break

days, hours = divmod(number, 86400)  # считаем дни, остача - часы
hours, minutes = divmod(hours, 3600)  # считаем часы, остача - минуты
minutes, seconds = divmod(minutes, 60)  # считаем минуты, остача - секунды

print(f"{number} -> {days} Days, {hours:02}:{minutes:02}:{seconds:02}")