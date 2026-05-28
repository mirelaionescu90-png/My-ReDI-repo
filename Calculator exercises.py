number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_division = number1 // number2
remainder = number2 % number1

print(f"{number1} + {number2} = {addition} ")
print(f"{number1} - {number2} = {subtraction} ")
print(f"{number1} * {number2} = {multiplication} ")
print(f"{number1} / {number2} = {division} ")
print(f"{number1} //{number2} = {floor_division} ")
print(f"{number1} % {number2} = {remainder} ")
print(f"The remainder of {number1} divided by {number2} is {remainder}")