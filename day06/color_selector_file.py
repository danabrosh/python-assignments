colors = open("colors.txt").read().splitlines()

for i in range(len(colors)):
    print(f"{i}: {colors[i]}")

choice = input("Please enter number: ")

if choice.isdigit():
    index = int(choice)
    if 0 <= index < len(colors):
        print("The selected color is:", colors[index])
    else:
        print("The number out of range.")
else:
    print("Invalid input. Please enter a whole number.")
