points_ = folds_ = None

with open("input.txt", "r") as f:
    points_, folds_ = f.read().split("\n\n")
points_ = [line for line in points_.splitlines()]
folds_ = [line for line in folds_.splitlines()]

points = set()
folds = []
for point in points_:
    i, j = point.split(",")
    i = int(i)
    j = int(j)
    point = (i, j)
    points.add(point)
for fold in folds_:
    fold = fold.split()[-1].split("=")
    fold[-1] = int(fold[-1])
    folds.append(fold)

def fold_paper(axis, line, points):
    coord = 0 if axis == "x" else 1
    new_points = {point for point in points if point[coord] <= line}
    invalid_points = {point for point in points if point[coord] > line}
    print(new_points and invalid_points)
    for point in invalid_points:
        if axis == "x":
            new_points.add((line - (point[0] - line), point[1]))
        else:
            new_points.add((point[0], line - (point[1] - line)))
    return new_points

# Part A
# fold_paper(*folds[0], points)

# Part B
new_points = points
for fold in folds:
    new_points = fold_paper(*fold, new_points)
from pprint import pprint
pprint(new_points)
