import copy

data = open("input.txt", "r").read().strip().split("\n\n")
DECODE_STR = "".join("0" if ch == "." else "1" for ch in data[0])

NEIGHBOURS = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]


def wrap_grid(grid, wrap_with):
    grid_y = len(grid[0])
    new_grid = [[wrap_with for _ in range(grid_y + 2)]]
    for row in grid:
        wrapped_row = [wrap_with]
        wrapped_row.extend(row)
        wrapped_row.append(wrap_with)
        new_grid.append(wrapped_row)
    new_grid.append([wrap_with for _ in range(grid_y + 2)])
    return new_grid


def lookup(grid, row, col, default):
    bstr = ""
    for dx, dy in NEIGHBOURS:
        x_ = row + dx
        y_ = col + dy
        if 0 <= x_ < len(grid) and 0 <= y_ < len(grid[0]):
            bstr += grid[row + dx][col + dy]
        else:
            bstr += default

    idx = int(bstr, 2)
    return DECODE_STR[idx]


def enchance(grid, wrap_with):
    wrapped_grid = wrap_grid(grid, wrap_with=wrap_with)
    outp_grid = copy.deepcopy(wrapped_grid)
    for row in range(0, len(wrapped_grid)):
        for col in range(0, len(wrapped_grid[0])):
            new_cell = lookup(wrapped_grid, row, col, default=wrap_with)
            outp_grid[row][col] = new_cell
    return outp_grid


grid = [["0" if ch == "." else "1" for ch in row] for row in data[1].split("\n")]

for i in range(50):  # range is 2 for part a, 50 for part b
    if DECODE_STR[0] == "0":
        wrap_with = "0"
    else:
        # This is assuming that the expected output isn't infinity, which would break the puzzle
        wrap_with = str(i & 1)
    grid = enchance(grid, wrap_with=wrap_with)

ans = 0
for row in grid:
    ans += sum(map(int, row))
print(ans)

