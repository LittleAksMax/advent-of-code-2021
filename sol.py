if __name__ == '__main__':
    data = None
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # Part 1
    # gamma, epsilon = "", ""
    # for col in range(12):
    #     ones, zeroes = 0, 0
    #     for row in range(len(data)):
    #         if data[row][col] == "0":
    #             zeroes += 1
    #         elif data[row][col] == "1":
    #             ones += 1
    #     if ones > zeroes:
    #         gamma += "1"
    #         epsilon += "0"
    #     elif zeroes > ones:
    #         gamma += "0"
    #         epsilon += "1"
    # print(gamma, epsilon)
    # gamma = int(gamma, 2)
    # epsilon = int(epsilon, 2)

    # print(gamma * epsilon)

    # Part 2
    co = xo = None
    for b in [True, False]:
        values = [int(x, 2) for x in data]
        for i in range(11, -1, -1):
            criterion = (1 if (sum([x >> i & 1 for x in values]) > (len(values) / 2)) else 0) << i
            if len([x for x in values if (x & (1 << i)) == criterion]) == (len(values) / 2):
                if b:
                    values = [x for x in values if (x & (1 << i)) > 0]
                else:
                    values = [x for x in values if (x & (1 << i)) == 0]
            else:
                if b:
                    values = [x for x in values if (x & (1 << i)) == criterion]
                else:
                    values = [x for x in values if (x & (1 << i)) != criterion]
            if len(values) == 1:
                if b:
                    co = values[0]
                else:
                    xo = values[0]
    print(xo * co)

        