
def get_fuel(number, part):
    if part == 1:
        return number
    else:
        return ((number * number) + number) // 2


def solution(part):
    input_data = None
    with open("input.txt", "r") as f:
        input_data = [int(i) for i in f.read().split(",")]
    min_fuel = None
    best_position = None

    for number in input_data:
        curr_position = number
        curr_fuel = 0

        for num in input_data:
            if num != number:
                curr_fuel += get_fuel(abs(curr_position - num), part)

        if min_fuel is None or curr_fuel < min_fuel:
            min_fuel = curr_fuel
            best_position = curr_position

    print(f"Part {part}: {min_fuel}")

solution(1)
solution(2)