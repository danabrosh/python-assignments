import random
# random number between 1-20
random_number = random.randint(1, 20)
guess_correct = False

while not guess_correct:
    input_number = int(input("Choose a number between 1-20: "))
    
    if random_number < input_number:
        print(f"Your guess {input_number} is higher than the random number.")
    elif random_number > input_number:
        print(f"Your guess {input_number} is lower than the random number.")
    else:
        print(f"Your guess {input_number} is equal to the random number.")
        guess_correct = True
