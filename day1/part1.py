with open("D:\Project\Advent_of_Code_2025\day1\input.txt") as file:
    lines = [line.rstrip() for line in file]

dial = 50
click = 0

for move in lines:
    direction, number = move[:1], int(move[1:])
    
    if direction == "R":
        dial += number
    else:
        dial -= number
    
    click += abs(dial // 100)
    dial = abs(dial) % 100

print(click)
    

