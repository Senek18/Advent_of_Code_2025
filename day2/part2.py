import math


def find_divisors(number):    
    divisors = set()

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            
            pair_divisor = number // i
            divisors.add(pair_divisor)

    result = sorted(list(divisors))
    result.remove(number)
    return result

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

        for slide in find_divisors(id_len):
            all_numbers = [id_str[i:i + slide] for i in range(0, len(id_str), slide)]
            if len(set(all_numbers)) == 1:
                list_of_id.append(id)
                break
        

print(sum(list_of_id))