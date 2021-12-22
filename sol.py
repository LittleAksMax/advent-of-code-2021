from re import findall
from math import prod
from collections import Counter


def part1():
    on = set()
    for l in open("input.txt").read().splitlines():
        coor = list(map(int, findall(r"-?\d+", l)))
        assert coor[1] >= coor[0]
        assert coor[3] >= coor[2]
        assert coor[5] >= coor[4]
        if (
            coor[0] > 50
            or coor[1] < -50
            or coor[2] > 50
            or coor[3] < -50
            or coor[4] > 50
            or coor[5] < -50
        ):
            continue
        if "on" in l:
            for x in range(max(coor[0], -50), min(50, coor[1]) + 1):
                for y in range(max(coor[2], -50), min(50, coor[3]) + 1):
                    for z in range(max(coor[4], -50), min(50, coor[5]) + 1):
                        on.add((x, y, z))
        else:
            for x in range(max(coor[0], -50), min(50, coor[1]) + 1):
                for y in range(max(coor[2], -50), min(50, coor[3]) + 1):
                    for z in range(max(coor[4], -50), min(50, coor[5]) + 1):
                        on.discard((x, y, z))

    print(len(on))

def intersection(cuboid1, cuboid2):
    inter = [
        min(c1, c2) if k % 2 else max(c1, c2)
        for k, (c1, c2) in enumerate(zip(cuboid1, cuboid2))
    ]
    if all(m <= M for m, M in zip(inter[::2], inter[1::2])):
        return tuple(inter)


def volume(cuboid):
    return prod((M - m + 1 for m, M in zip(cuboid[::2], cuboid[1::2])))


def part2():
    def parse_line(line):
        on, cuboid = line.split(" ")
        ranges = findall(r"-?\d+", cuboid)
        return on == "on", tuple(map(int, ranges))
    data = [parse_line(l) for l in open("input.txt").read().splitlines()]
    cuboids = Counter([data[0][1]])
    for action, span in data[1:]:
        for cuboid, flag in cuboids.copy().items():
            intersect = intersection(cuboid, span)
            if intersect is not None:
                cuboids[intersect] += -flag
        if action:
            cuboids[span] += 1
        cuboids = Counter({c: f for c, f in cuboids.items() if f})
    print(sum(flag * volume(c) for c, flag in cuboids.items()))

# part1()
part2()

