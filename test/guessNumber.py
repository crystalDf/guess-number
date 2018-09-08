import random

target = random.randint(1, 10)
time = 3

print("Please guess a number between 1-10")

while True:
    try:
        guess = int(input())
        if (guess > 10) or (guess < 1):
            raise ValueError()
        if guess < target:
            print("less")
        elif guess > target:
            print("larger")
        else:
            print("right")
            break
        time -= 1
        if time == 0:
            print("you lose")
            break
    except ValueError:
        print("You should enter an int number between 1-10")
