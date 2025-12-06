with open("D:\Project\Advent_of_Code_2025\day3\input_.txt") as file:
    banks_list = [line.rstrip() for line in file]

output = []

def find_max(number):
    number_list = list(number)
    highest_digit = max(number_str)
    highest_digit_index = number_str.rfind(highest_digit)
    number_list[highest_digit_index] = "0"
    return "".join(number_list), highest_digit, highest_digit_index
234234234234278
874444333322
343434234278
434234234278

for number_str in banks_list:
    numbers_list = []
    index_list = []

    for _ in range(12):
        number_str, highest_digit, highest_digit_index = find_max(number_str)
        numbers_list.append(highest_digit)
        index_list.append(highest_digit_index)
    print(index_list)
    zipped = zip(index_list, numbers_list)
    sorted_list = sorted(zipped)
    _, sorted_numbers = zip(*sorted_list)
    joltage = "".join(sorted_numbers)
    print(joltage)
    output.append(int(joltage))

print(sum(output))