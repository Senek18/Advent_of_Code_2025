with open("D:\Project\Advent_of_Code_2025\day1\input.txt") as file:
    lines = [line.rstrip() for line in file]

dial = 50
click = 0

for move in lines:
    direction, number = move[:1], int(move[1:])

    if direction == "R":
        for i in range(number):
            dial = dial + 1 
            if dial == 100:
                dial = 0
            
            if dial == 0:
                click += 1
            
    else:
        for i in range(number):
            dial = dial - 1
            if dial == 0:
                click += 1
            if dial == -1:
                dial = 99

print(click)