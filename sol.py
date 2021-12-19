from re import findall
from itertools import combinations

with open("input.txt", "r") as f:
    text = f.read().strip()

get_vec = lambda line: tuple(map(int, findall('-?\d+', line)))
data = [set(map(get_vec, area.split('\n')[1:])) for area in text.split('\n\n')]

sub = lambda a, b: tuple(x-y for x,y in zip(a,b))
add = lambda a, b: tuple(x+y for x,y in zip(a,b))

def make_offset_table(lst):
    return { p: set(sub(p,q) for q in lst) for p in lst }

def orient(pt, orientation):
    a, b, c = pt
    return [
        (+a,+b,+c), (+b,+c,+a), (+c,+a,+b), (+c,+b,-a), (+b,+a,-c), (+a,+c,-b), 
        (+a,-b,-c), (+b,-c,-a), (+c,-a,-b), (+c,-b,+a), (+b,-a,+c), (+a,-c,+b), 
        (-a,+b,-c), (-b,+c,-a), (-c,+a,-b), (-c,+b,+a), (-b,+a,+c), (-a,+c,+b), 
        (-a,-b,+c), (-b,-c,+a), (-c,-a,+b), (-c,-b,-a), (-b,-a,-c), (-a,-c,-b) 
    ][orientation]

def all_possible_orientations(pts):
    return ((i, set(orient(x, i) for x in pts)) for i in range(24))

def enough_common_points(offs1, offs2):
    for x, xv in offs1.items():
        for y, yv in offs2.items():
            if len(xv & yv) >= 12:  # & -> intersection
                return sub(x, y)

def do_scanners_match(scanner1, scanner2):
    offsets1 = make_offset_table(scanner1)
    for orientation, beacons in all_possible_orientations(scanner2):
        offsets2 = make_offset_table(beacons)
        if result := enough_common_points(offsets1, offsets2):
            return result, orientation

remaining = data.copy()
beacons = remaining.pop(0)
locations = {(0,0,0)}

while remaining:
    for i, d in enumerate(remaining):
        if result := do_scanners_match(beacons, d):
            offset, ori = result
            locations.add(offset)
            beacons |= {add(orient(b, ori), offset) for b in d} # | -> union
            remaining.pop(i)
            break

max_dist = max(
    sum(abs(x-y) for x,y in zip(a,b)) 
    for a,b in combinations(locations, 2)
)

# part 1
print(len(beacons))
# part 2
print(max_dist)