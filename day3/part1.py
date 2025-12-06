with open("D:\Project\Advent_of_Code_2025\day3\input_.txt") as file:
    banks_list = [line.rstrip() for line in file]
output = []
for number_str in banks_list:
    highest_digit = max(number_str)
    highest_digit_index = number_str.find(highest_digit)
    if highest_digit_index == len(number_str) - 1 and highest_digit == '9':
        new_number_str = number_str[:highest_digit_index]
        next_highest_digit = max(new_number_str)
        joltage = next_highest_digit + highest_digit
    elif highest_digit_index == len(number_str) - 1:
        next_highest_digit = number_str[highest_digit_index-1]
        joltage = next_highest_digit + highest_digit
    else:
        new_number_str = number_str[highest_digit_index+1:]
        next_highest_digit = max(new_number_str)
        joltage = highest_digit + next_highest_digit

    output.append(int(joltage))
print(sum(output))