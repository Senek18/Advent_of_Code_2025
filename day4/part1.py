with open("D:\Project\Advent_of_Code_2025\day4\input.txt") as file:
    diagram = [line.rstrip() for line in file]

x_shape = len(diagram[0])
y_shape = len(diagram)

moves = {
    "L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0),
    "LU": (1, -1), "LD": (-1, -1), "RU": (1, 1), "RD": (-1, 1)
}

access = 0

for y in range(y_shape):
    for x in range(x_shape):    
        if diagram[y][x] == ".":
            continue
        papper_rolls = 0

        for y_add, x_add in moves.values():
            x_new = x + x_add
            if x_new > x_shape-1 or x_new < 0:
                continue

            y_new = y + y_add
            if y_new > y_shape-1 or y_new < 0:
                continue
            
            if diagram[y_new][x_new] == "@":
                papper_rolls += 1
            
        if papper_rolls < 4:
            access += 1

print(access)
