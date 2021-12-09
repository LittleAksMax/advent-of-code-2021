data = None
with open("input.txt", "r") as f:
    data = [i for i in f.read().splitlines()]
    data = [list(i) for i in data]
    data = [[int(y) for y in x] for x in data]

# Part A
# count = 0
# for row_idx, row in enumerate(data):
#     for col_idx, cur in enumerate(row):
#         if row_idx > 0:
#             if data[row_idx - 1][col_idx] > cur:
#                 pass
#             else: continue
#         if row_idx < len(data) - 1:
#             if data[row_idx + 1][col_idx] > cur:
#                 pass
#             else: continue
#         if col_idx > 0:
#             if data[row_idx][col_idx - 1] > cur:
#                 pass
#             else: continue
#         if col_idx < len(row) - 1:
#             if data[row_idx][col_idx + 1] > cur:
#                 pass
#             else: continue
#         # valid.append((row_idx), (col_idx))
#         count += 1 + cur
# print(count)

# Part B
def get_basin(matrix, i, j):
    if not (0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] != 9):
        return 0
    # don't bother with visited, just set to 9
    matrix[i][j] = 9
    # recursive call to its neighbours
    return (
        1
        + get_basin(matrix, i - 1, j)
        + get_basin(matrix, i + 1, j)
        + get_basin(matrix, i, j - 1)
        + get_basin(matrix, i, j + 1)
    )

basins = []
for i in range(len(data)):
    for j in range(len(data[i])):
        basins.append(get_basin(data, i, j))
basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])