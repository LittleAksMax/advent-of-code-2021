
if __name__ == "__main__":
    data = []
    with open("input.txt", "r") as f:
        data = f.read().split("\n")
    data = [int(i) for i in data]
    count = 0
    # Part 1
    # for depth in range(1, len(data)):
    #     if data[depth] > data[depth - 1]: count += 1
    # Part 2
    prev_sum = -1
    for depth in range(len(data)):
        if depth > len(data) - 3: continue
        sum_ = data[depth] + data[depth + 1] + data[depth + 2]
        if prev_sum != -1:
            if sum_ > prev_sum: count += 1
        prev_sum = sum_

    print(count)