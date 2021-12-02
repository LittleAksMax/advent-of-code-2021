
if __name__ == '__main__':
    data = None
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [i.split(" ") for i in data]
    depth = 0
    horiz = 0

    # Part 1
    # for inst in data:
    #     if inst[0] == "forward":
    #         horiz += int(inst[1])
    #     elif inst[0] == "down":
    #         depth += int(inst[1])
    #     elif inst[0] == "up":
    #         depth -= int(inst[1])
    
    # Part 2
    aim = 0
    for inst in data:
        if inst[0] == "forward":
            horiz += int(inst[1])
            depth += aim * int(inst[1])
        elif inst[0] == "down":
            aim += int(inst[1])
        elif inst[0] == "up":
            aim -= int(inst[1])

    print(depth * horiz)