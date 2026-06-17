import random

number = random.randint(1,100)

attempts = 0

while True:
    user_number = int(input ("Enter your Number to Guess (1 - 100) \n"))
    attempts += 1

    if number < user_number:
        print("Too High")
    elif number > user_number:
        print("Too Low")
    else:
        print(f"you guess a number in {attempts} attempts\n")
        break