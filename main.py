import random

# 5-1 Conditional tests - new file ?
car = ''
cars = ["Subaru", "Audi", "VW", "Opel", "Koenigsegg"]

# picking a car from the list and assigning it to a String
car = cars[0]

# testing the build of the car
print("Is car == 'subaru'? I predict this to be True")
print(car.lower() == 'subaru')

print("\nIs cars == 'audi? I predict this to be False")
print(car.lower() == 'audi')


# picking a new car, this time a random
car = random.choice(cars)

# testing for the make of the car - I predict 4 False and 1 True

print("Is car == 'subaru'?")
print(car.lower() == 'subaru')

print("Is cars == 'audi?")
print(car.lower() == 'audi')

print("Is car == 'vw'?")
print(car.lower() == 'vw')

print("Is cars == 'opel?")
print(car.lower() == 'opel')

print("Is cars == 'koenigsegg?")
print(car.lower() == 'koenigsegg')

# smarter coding

# picking a new car, this time a random
car = random.choice(cars)

# counter
count = 0

# testing for the make of the car - I predict 4 False and 1 True
while count < len(cars):
    print(f"Is the car in question a {cars[count]}? - {car.lower() == cars[count].lower()}")
    count += 1

alien_color = "green"

# 5-4 alien color
if alien_color == "red":
    print("\nYou earned 5 points")
else:
    print("You earned 10 points")

# 5-5 alien color - expanded
if alien_color == "red":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")

# 5-6 stages of life
print("\n")
age = 17
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

# 5-7 favourite fruit
print("\n")
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")
if 'beef' in favorite_fruits:
    print("Beef is not fruit")

# 5-8 Hello admin 5-9 No users
print("\n")
usernames = ["Jens", "Anders", "Admin", "Viktorija", "Gosia"]

if usernames:
    for username in usernames:
        if username == "Admin":
            print(f"Hello {username}, do you want to see the status report?")
        else:
            print(f"Hello {username}, welcome back!")
else:
    print("We need users!")

# 5-10 new user check
print("\n")
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry, that username is already taken")
    else:
        print(f"Welcome {new_user}")

#  5-11 ordinal numbers
print("\n")
numbers = list(range(1,40))

for number in numbers:
    if number == 1 or number == 11 or number == 21 or number == 31:
        print(f"{number}st")
    elif number == 2 or number == 12 or number == 22 or number == 32:
        print(f"{number}nd")
    elif number == 3 or number == 13 or number == 23 or number == 33:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# 5-12 and 5-13 Styling code and ideas for solving real life issues.
# committed from beta to version 1.0 with some difficulties

print("\nExit program")
