from typing import DefaultDict

class Octopus:
    def __init__(self, lines):
        self.octopi = DefaultDict(lambda: 10)

        x = 0
        for line in data:
            y = 0
            for c in line:
                self.octopi[(x, y)] = int(c)
                y +=1
            x += 1

        self.rows = x
        self.cols  = y

    def max_flashes(self):
        return self.rows * self.cols

    def step(self):
        flashes = 0
        q = []
        for x in range(0, self.rows):
            for y in range(0, self.cols):
                q.append((x, y))

        while len(q) > 0:
            (x, y) = q.pop()
            self.octopi[(x, y)] += 1
            if self.octopi[(x, y)] == 10:
                # add all neighbours
                flashes += 1
                q.append((x - 1, y - 1))
                q.append((x - 1, y))
                q.append((x - 1, y + 1))
                q.append((x, y - 1))
                q.append((x, y + 1))
                q.append((x + 1, y - 1))
                q.append((x + 1, y))
                q.append((x + 1, y + 1))

        for x in range(0, self.rows):
            for y in range(0, self.cols):
                if self.octopi[(x, y)] >= 10:
                    self.octopi[(x, y)] = 0

        return flashes

data = None
with open("input.txt", "r") as f:
    data = [l.strip() for l in open("input.txt", "r").readlines()]

octopi = Octopus(data)
total_flashes = 0

i = 0
while True:
    i += 1
    new_flashes = octopi.step()
    total_flashes += new_flashes
    print(f"step: {i} total: {total_flashes}")
    if new_flashes == octopi.max_flashes():
        break
