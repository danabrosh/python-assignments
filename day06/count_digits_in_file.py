def count_digits(lst):
    counts = [0] * 10 

    for number in lst:
        for digit in str(number):
            counts[int(digit)] += 1
    
    return counts

filename = input("Enter filename: ")

with open(filename, 'r') as f:
    numbers = [int(num) for num in f.read().split()]

counts = count_digits(numbers)

with open('report.txt', 'w') as f:
    for i in range(10):
        f.write(f"{i} {counts[i]}\n")
