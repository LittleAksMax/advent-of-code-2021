from itertools import cycle
from functools import lru_cache

with open("input.txt", "r") as f:
    data = f.read().splitlines()
    p1_pos = int(data[0].split(": ")[1])
    p2_pos = int(data[1].split(": ")[1])


def move(pos, score, amount):
    pos = (pos + amount - 1) % 10 + 1
    return pos, score + pos

def practice(a, b):
    players = [(a, 0), (b, 0)]
    die = cycle(range(1, 101))
    rolls = 0
    while True:
        for player, (pos, score) in enumerate(players):
            roll = next(die) + next(die) + next(die)
            rolls += 3
            pos, score = players[player] = move(pos, score, roll)
            if score >= 1000:
                _, otherscore = players[1 - player]
                return rolls * otherscore

def play(a, b):
    @lru_cache(maxsize=None)
    def count_wins(a, b):
        awins = bwins = 0
        for x in range(1, 4):
            for y in range(1, 4):
                for z in range(1, 4):
                    _, score = roll_a = move(a[0], a[1], x + y + z)
                    if score >= 21:
                        awins += 1
                    else:
                        roll_bwins, roll_awins = count_wins(b, roll_a)
                        awins += roll_awins
                        bwins += roll_bwins
        return awins, bwins
    return max(count_wins((a, 0), (b, 0)))

# print(practice(p1_pos, p2_pos))
print(play(p1_pos, p2_pos))

# die = 1
# p1 = p2 = 0
# turn = "p1"
# while p1 < 1000 and p2 < 1000:
#     for _ in range(3):
#         if turn == "p1":
#             p1_pos = p1_pos + die
#             if p1_pos > 10: p1_pos -= 10
#         else:
#             p2_pos = p2_pos + die
#             if p2_pos > 10: p2_pos -= 10
#         die += 1
#         if die > 100:
#             die -= 100
#     if turn == "p1":
#         p1 += p1_pos
#     else:
#         p2 += p2_pos
#     turn = "p1" if turn == "p2" else "p2"

# print(p1 * p2)
