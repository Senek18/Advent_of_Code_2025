from functools import reduce
import operator

with open("D:\Project\Advent_of_Code_2025\day6\input.txt") as file:

    problems = [line.rstrip().split(" ") for line in file]

for row in problems:
    while "" in row:
        row.remove("")

y_shape = len(problems) - 1
x_shape = len(problems[0])

numbers = []

for x in range(x_shape):
    column = []
    for y in range(y_shape):
        column.append(int(problems[y][x]))

    numbers.append(column)

final_sum = 0

for sign, column in zip(problems[-1], numbers):
    if sign == "+":
        result = sum(column)
    elif sign == "*":
        result = reduce(operator.mul, column)
    
    final_sum += result

print(final_sum)