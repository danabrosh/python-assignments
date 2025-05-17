def count_digits(lst):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    counts = [0] * 10 

    for number in lst:
        for digit in str(number):
            counts[int(digit)] += 1

    for i in numbers:
        print(i, counts[i])
    