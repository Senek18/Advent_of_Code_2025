with open("D:\Project\Advent_of_Code_2025\day5\input.txt") as file:
    stop = 0
    ranges = []
    ingredients = []

    for line in file:
        line = line.rstrip()
        if line == "":
            stop = 1
            continue
        
        if stop == 0:
            ranges.append(line)
        else:
            ingredients.append(int(line))
        

def merge_overlapping_intervals(intervals_str):

    intervals = []
    for interval_str in intervals_str:
        start, end = map(int, interval_str.split('-'))
        intervals.append((start, end))

    intervals.sort(key=lambda x: x[0])
    merged = []
    if not intervals:
        return []
    
    current_start, current_end = intervals[0]
    for next_start, next_end in intervals[1:]:
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    merged.append((current_start, current_end))
    result_str = [range(start, end+1) for start, end in merged]
    return result_str

ranges_merged = merge_overlapping_intervals(ranges)

fresh = 0
for ingredient in ingredients:
    for range in ranges_merged:
        if ingredient in range:
            fresh += 1
            continue

print(fresh)