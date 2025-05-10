import random
# random number between 1-20
random_number = random.randint(1, 20)

input_number = int(input("Choose a number between 1-20"))

if random_number < input_number:
    print(f"Your guess {input_number} is lower than the random number {random_number}.")
elif random_number > input_number:
    print(f"Your guess {input_number} is higher than the random number {random_number}.")
else:
    print(f"Your guess {input_number} is equal to the random number.")
