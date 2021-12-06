
CYCLE = 7
INITIAL_VALUE = 8
memoized_offspring_count_of_fish_for_remaining_days = {}

def calculate_offspring_count_of_fish(fish_timer, remaining_days):
    if (fish_timer, remaining_days) in memoized_offspring_count_of_fish_for_remaining_days:
        return memoized_offspring_count_of_fish_for_remaining_days[(fish_timer, remaining_days)]

    if remaining_days < fish_timer:
        return 0

    list_of_remaining_days_per_child = []

    next_child_remainibg_days = remaining_days - fish_timer - 1  # subtract -1 because
    while next_child_remainibg_days >= 0:
        list_of_remaining_days_per_child.append(next_child_remainibg_days)
        next_child_remainibg_days -= CYCLE

    offsprings_total_count = len(list_of_remaining_days_per_child)
    for r in list_of_remaining_days_per_child:
        offsprings_total_count += calculate_offspring_count_of_fish(INITIAL_VALUE, r)

    memoized_offspring_count_of_fish_for_remaining_days[(fish_timer, remaining_days)] = offsprings_total_count

    return offsprings_total_count
    

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    data = [int(x) for x in lines[0].strip().split(",")]

    part1_result = len(data)
    for f in data:
        part1_result += calculate_offspring_count_of_fish(f, 80)

    print(part1_result)

    # Part B
    # part2_result = len(data)
    # for f in data:
    #     part2_result += calculate_offspring_count_of_fish(f, 256)

    # print(part2_result)