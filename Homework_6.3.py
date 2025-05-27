# Добуток чисел

import string

letters = list(string.ascii_letters)
punctuation = list(string.punctuation)

###

while True:

    number = input("Enter your number: ")

    if (
        not number.isdigit()
    ):

        print("You have to type in a number")
        continue
    else:
        break

###

while int(number) > 9:
    result = 1
    for i in number:
        result = int(i) * result
    number = str(result)

print(f"Your result is: {number}")


















