#Перемістити елемент у списку


#First example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.pop(9)
numbers.insert(0, 10)
print(f"First example: {numbers}")

#Second example

players = ["john", "Max", "Jacob", "Andrew"]
players.pop(3)
players.insert(0, "Andrew")
print(f"Second example: {players}")