# Список із 3 елементів

import random

newlist = []

mylist = [random.randint(1, 10) for i in range(random.randint(3, 10))]

print(f"First list: {mylist}")

newlist.append(mylist[0])
newlist.append(mylist[2])
newlist.append(mylist[-2])

print(f"End list: {newlist}")

