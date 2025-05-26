#Діапазон букв

import string

letters = list(string.ascii_letters)

while True:

    imported_letters = input("Enter two letters (a-b): ")
    print()

    if (
            len(imported_letters) != 3 or
            imported_letters[1] != "-" or
            imported_letters[0] not in letters or
            imported_letters[2] not in
            letters

    ):

        print("You must write it again!\nDon't forget about '-' between letters.")
        print()
        continue
    else:
        break

first_letter = imported_letters[0]
second_letter = imported_letters[2]


first_index = letters.index(first_letter)

second_index = letters.index(second_letter)


result = "". join(letters[first_index:second_index + 1])
print(f"Your result is: {result}")






















