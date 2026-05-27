print("Hello,World!")
name = "Alice"
age = 30
height = 1.72
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

price = 19.99
quantity = 3

total = price * quantity
print(f"Total: {total}")

age = 30
birth_year = 2026 - age
print(f"Born in: {birth_year}")

minutes = 137
hours = minutes //60
remaining = minutes % 60
print(f"{hours}h {remaining}min")

first = "Hello"
second = "World"
print(first + " " + second)
print("ha" * 3)
print(len("Python"))

name = " alice "

print(name.upper())
print(name.lower())
print(name.strip())
print(name.strip().capitalize())

greeting = "Hello, World!"
print(greeting.replace("World", "Python"))

name = "Alice"
age = 30

print("Hello!")
print(name)
print("My name is", name)
print("Age:", age)

name = input("What is your name? ")
print(("Hello,", name))

age = input("How old are you? ")
print(type(age))

name = "Alice"
age = 30
city = "Copenhagen"

print(f"My name is {name}, I am {age} years old.")
print(f"I live in {city} .")

age_str = input("How old are you? ")
age = int(age_str)
height_str = "1.72"
height = float(height_str)
number = 42
text = str(number)

name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("What city are you from? ")
print(f"Nice to meet you, {name}!")
print(f"You are {age} years old and you are from {city}.")
print(f"In 10 years, you will be {age + 10}.")

