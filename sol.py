
if __name__ == '__main__':
    data = None
    with open("input.txt", "r") as f:
        data = [[pair for pair in line.split(" -> ")] for line in f.read().splitlines()]
    for pair in data:
        pair[0] = pair[0].split(",")
        pair[0] = [int(i) for i in pair[0]]

        pair[1] = pair[1].split(",")
        pair[1] = [int(i) for i in pair[1]]
    ignorediag = True # True for part A, false for part B 
    points = {}
    for pair in data:
        x1, y1 = pair[0][0], pair[0][1] 
        x2, y2 = pair[1][0], pair[1][1]
        if x1 == x2:  # vertical line
            start_point = f"{x1},{y1}"
            points[start_point] = 1 if start_point not in points.keys() else points[start_point] + 1
            temp = y1
            while temp != y2:
                temp = temp + 1 if temp < y2 else temp - 1
                point = f"{x1},{temp}"
                points[point] = 1 if point not in points.keys() else points[point] + 1

        elif y1 == y2: # horizontal line
            start_point = f"{x1},{y1}"
            points[start_point] = 1 if start_point not in points.keys() else points[start_point] + 1
            temp = x1
            while temp != x2:
                temp = temp + 1 if temp < x2 else temp - 1
                point = f"{temp},{y1}"
                points[point] = 1 if point not in points.keys() else points[point] + 1

        elif not ignorediag and abs(x2-x1) == abs(y2-y1): # vertical line at 45 degrees
            start_point = f"{x1},{y1}"
            points[start_point] = 1 if start_point not in points.keys() else points[start_point] + 1
            temp_x = x1
            temp_y = y1
            while temp_x != x2:
                temp_x = temp_x + 1 if temp_x < x2 else temp_x - 1
                temp_y = temp_y + 1 if temp_y < y2 else temp_y - 1
                point = f"{temp_x},{temp_y}"
                points[point] = 1 if point not in points.keys() else points[point] + 1
    count = 0
    for coord in points.keys():
        if points[coord] > 1:
            count += 1
    print(count)

