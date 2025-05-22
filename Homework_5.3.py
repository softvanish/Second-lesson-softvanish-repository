#hashtag

import string


punctuation = list(string.punctuation)


while True:

###

    hashtag = input(str("Enter your hashtag: "))

###

    if any(symbol in punctuation for symbol in hashtag):

        print()

        print("You cannot use punctuation symbols")

        print()

###

        print("____" * 10)

        print()

        next = input("Do you want to try again? (Yes or Not): ")

        print()

        print("____" * 10)

###

        if next.title() != "Yes":
             print("Bye!")
             break

        else:
            continue

###

    for i in hashtag:
        hashtag_with_title = hashtag.title()
        hashtag_with_split = hashtag_with_title.split()
        new_hash = "".join(hashtag_with_split)
        new_hash1 = "#" + new_hash

    new_hash1 = new_hash1[:140]


    print(len(new_hash1))

    print(new_hash1)

###

    print("____" * 10)

    next = input("Do you want to try again? (Yes or Not): ")

    print("____" * 10)

    if next.title() != "Yes":
        print("Bye!")
        break
