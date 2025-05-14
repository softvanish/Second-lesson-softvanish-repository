print("We will multiply your numbers!")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def multiply(num1, num2):
    return num1 * num2

result = multiply(num1, num2)
print(f"Your answer is: {result}")
