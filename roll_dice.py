import random
choice = input(f"roll the dice? (y/n):").lower()
while True:
    if choice == 'y':

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}")
        choice = input(f"roll the dice? (y/n):").lower()
    elif choice == "n":
        print("thanks for playing ")
        break
    else:
        print("invalid number")
