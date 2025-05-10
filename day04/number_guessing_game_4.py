import random

random_number = random.randint(1, 20)
guess_correct = False
debug_mode = False

while not guess_correct:
    if debug_mode:
        print(f"[DEBUG] Current number to guess: {random_number}")
    
    user_input = input("Choose a number between 1-20 ('x' to exit, 'd' to toggle debug): ")
    
    if user_input == 'x':
        print("Game ended.")
        break
    elif user_input == 's':
        print(f"The hidden number is: {random_number}")
        continue
    elif user_input == 'd':
        debug_mode = not debug_mode
        print(f"Debug mode {'enabled' if debug_mode else 'disabled'}")
        continue
    
    input_number = int(user_input)
    
    if random_number < input_number:
        print(f"Your guess {input_number} is higher than the random number.")
    elif random_number > input_number:
        print(f"Your guess {input_number} is lower than the random number.")
    else:
        print(f"Your guess {input_number} is equal to the random number.")
        guess_correct = True
