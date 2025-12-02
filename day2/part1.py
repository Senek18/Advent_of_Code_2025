with open("D:\Project\Advent_of_Code_2025\day2\input_.txt") as file:
    lines = [line.rstrip() for line in file]
    id_ranges = lines[0]

id_pairs = id_ranges.split(",")
list_of_id = []

for pair in id_pairs:
    start_id, end_id = pair.split("-")
    for id in range(int(start_id), int(end_id) + 1):
        id_str = str(id)
        id_len = len(id_str)
        if id_len % 2 == 0:
            p1 = id_str[:id_len // 2]
            p2 = id_str[id_len // 2:]
            if p1 == p2:
                list_of_id.append(id)

print(sum(list_of_id))