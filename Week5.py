raining = input("Is it raining? (yes/no) ")
if raining == "yes":
    print("Grab an umbrella!")

else:
    print("Enjoy the walk!")


weather = input("What is the weather like? ")

if weather == "storm":
    print("Stay inside!")
elif weather == "rain":
    print("Grab an umbrella!")
elif weather == "clouds":
    print("Bring a jacket!")
else:
    print("Enjoy the sunshine!")


weather = input("What is the weather like? ")

if weather == "storm":
    print("Stay inside!")

else:
    if weather == "rain":
        print("Grab an umbrella.")

    else:
        if weather == "clouds":
            print("Bring a jacket.")

        else:
            print("Enjoy the sunshine!")



has_map = False
has_signpost = True
has_stars = False
has_phone = True

if has_map:
    print("follow the map.")
elif has_signpost:
    print("Read the signpost.")
elif has_stars:
    print("Navigate by stars.")
elif has_phone:
    print("Check your GPS.")
else:
    print("Take a guess!")



has_internet = True
credentials_valid = True
can_read = True
can_write = False
enough_space = False

if has_internet:
    if credentials_valid:
        if can_read:
            print("Reading...")
        elif can_write:
            if enough_space:
                print("Writing...")
            else:
                print("Not enough space.")
        else:
            print("No operation.")
    else:
        print("Invalid credentials.")
else:
    print("No internet.")


answer = input("Continue? (Y/N) ")

if (answer != "y" and answer != "yes" and answer != "N" and answer != "no"):
    print("Invalid input.")
elif answer == "Y" or answer == "yes":
    print("Continuing!")
else:
    print("Stopping.")








    




