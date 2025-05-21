# Ім'я змінної



###

import keyword

import string

###

uppercase_letters = list(string.ascii_uppercase)

numbers = list(string.digits)

punctuation = list(string.punctuation)

###

test_data = input("Enter you variable: ")



if test_data in keyword.kwlist:
    print(f"Incorrect naming convention for potential variable: {test_data} ")
    exit()

if test_data[0] in numbers:
    print(f"Incorrect naming convention for potential variable: {test_data} ")
    exit()

for variab in test_data:

    if variab in uppercase_letters:
        print(f"Incorrect naming convention for potential variable: {test_data} " )
        exit()

    elif variab in punctuation:
        print(f"Incorrect naming convention for potential variable: {test_data}")
        exit()


print(f"Correct naming convention for potential variable: {test_data}")














