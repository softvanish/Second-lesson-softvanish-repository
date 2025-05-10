
user_num = int(input("Please enter your five-digit number: "))

num1, num2 = divmod(user_num, 10000)
num2, num3 = divmod(num2, 1000)
num3, num4 = divmod(num3, 100)
num4, num5 = divmod(num4, 10)

print(num5, num4, num3, num2, num1, sep= "")
