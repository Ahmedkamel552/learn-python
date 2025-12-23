import random


number = random.randint(1, 100)
while True:
    try:
        guess_number = int(input("guess a number between 1 to 100 "))
        if guess_number == number:
            print("you win")
            break
        elif guess_number < number:
            print("too low")
        elif guess_number > number:
            print("too high")
        else:
            print("invalid number")
            break
    except ValueError:
        print("enter a valid number")
