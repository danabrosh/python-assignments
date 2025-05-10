import random

playing = True
while playing:
    random_number = random.randint(1, 20)
    guess_correct = False
    debug_mode = False
    move_mode = False
    
    while not guess_correct:
        if debug_mode:
            print(f"[DEBUG] Current number to guess: {random_number}")
        
        user_input = input("Choose a number between 1-20 ('x' to exit, 'n' for new game, 'd' to toggle debug, 'm' to toggle move mode): ")
        
        if user_input == 'x':
            print("Game ended.")
            playing = False
            break
        elif user_input == 'n':
            print("Starting new game!")
            break
        elif user_input == 's':
            print(f"The hidden number is: {random_number}")
            continue
        elif user_input == 'd':
            debug_mode = not debug_mode
            print(f"Debug mode {'enabled' if debug_mode else 'disabled'}")
            continue
        elif user_input == 'm':
            move_mode = not move_mode
            print(f"Move mode {'enabled' if move_mode else 'disabled'}")
            continue
        
        input_number = int(user_input)
        
        if random_number < input_number:
            print(f"Your guess {input_number} is higher than the random number.")
        elif random_number > input_number:
            print(f"Your guess {input_number} is lower than the random number.")
        else:
            print(f"Your guess {input_number} is equal to the random number.")
            guess_correct = True
            print("Starting new game!")
            
        if move_mode and not guess_correct:
            random_number += random.randint(-2, 2)
            random_number = max(1, min(20, random_number))
