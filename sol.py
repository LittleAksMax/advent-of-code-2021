data = open("input.txt").read().splitlines()

height, width = len(data), len(data[0])
board = {(x, y): data[y][x] for y in range(height) for x in range(width)}
safe = None
step = 0
while safe != board:
    safe, step = board.copy(), step + 1
    east = [(x, y) for (x, y), e in board.items() if e == '>' and board.get(((x + 1) % width, y), '') == '.']
    for x, y in east:
        board[x, y],board[(x + 1) % width, y] = '.>'
    south = [(x, y) for (x, y), e in board.items() if e == 'v' and board.get((x, (y + 1) % height), '') == '.']
    for x, y in south:
        board[x, y], board[x, (y + 1) % height] = '.v'
print(step)
