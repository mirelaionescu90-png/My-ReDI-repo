age = 20
print(age >= 18)

price = 9.99
budget = 10.00
print(price <= budget)

password = "abc123"
print(password == "abc123")
print(password == "ABC123")

score = 85
print(score == 100)
print(score != 100)


age = 25
has_ticket = True
is_raining = False

print(age >= 18 and has_ticket)

print(age >= 18 or has_ticket)
print(age < 18 or has_ticket)

print(not is_raining)
print(not has_ticket)


age = int(input ("How old are you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 75:
    print("Grade: B - Good job!")
elif score >= 60:
    print("Grade: C- Passed.")
else:
    print("Grade: F - Better luck next time.")



age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? (yes/no) ")

if age >= 18 and has_ticket == "yes":
    print("Welcome! Enjoy the show.")
elif age >= 18 and has_ticket != "yes":
    print("You need a ticket to enter.")
elif age < 18 and has_ticket == "yes":
    print("Sorry, this event is 18+ ")
else:
    print("You need to be 18+ and have a ticket.")
    

age = int(input("How old are you? "))

if age >= 18:
    country = input("Which country are you from? ")
    if country == "Denmark":
        print("you can vote in Danish elections!")
    else:
        print("You are an adult, but not eligible for Danish elections.")
else:
    print("You are too young to vote.")


name = input("What is your name? ")

if name:
    print(f"Hello, {name}!")
else:
    print("You did not enter a name.")

score = int(input("Enter your score: "))
if score:
    print(f"You scored {score} points.")
else:
    print("You scored zero - better luck next time!")