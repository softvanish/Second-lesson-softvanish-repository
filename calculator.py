

###
class Calculator:
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        return a / b

calc = Calculator()

###
while True:

    print()

    print("It's my calculator, let's test it!")

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    operation = input("Choose your option \"+, -, *, /\": ")

    ###

    if operation == "+":
        calc.add(num1, num2)
        result = calc.add(num1, num2)

    elif operation == "-":
        calc.substract(num1, num2)
        result = calc.substract(num1, num2)

    elif operation == "*":
        calc.multiply(num1, num2)
        result = calc.multiply(num1, num2)

    elif operation == "/":
        calc.divide(num1, num2)
        result = calc.divide(num1, num2)

    else:
        print("Wrong")
        result = None

    ###

    if result is not None:
        print(f"Your result: {result} ")

