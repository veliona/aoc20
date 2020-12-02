from itertools import combinations

with open('data.csv.txt') as data:
    numbers = [int(line.strip()) for line in data]
    comb = combinations(numbers, 2)

    # Print the obtained combinations
    for i in list(comb):
        if sum(list(i)) == 2020:
            print(i[0] * i[1])
