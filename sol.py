data = None
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

count = 0

# Part A
# for line in data:
#     a, b = line.split('|')
#     x = a.split(' ')
#     y = b.split(' ')

#     for num in y:
#         if len(num) in {2, 4, 3, 7}:
#             count += 1

# Part B
d = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}
count = 0
for line in data:
    a, b = line.split('|')
    x = a.split(' ')
    y = b.split(' ')
	
    comb = [[] for _ in range(8)]
    fin = [0] * 10
    for num in (x + y):
        if not num:
            continue
        comb[len(num)].append(sorted(num))
	
    for i in range(8):
        comb[i] = list(map(list, set(map(tuple, comb[i]))))
	
    for i in range(len(comb)):
        if i == 2:
            fin[1] = comb[i][0]
        elif i == 4:
            fin[4] = comb[i][0]
        elif i == 3:
            fin[7] = comb[i][0]
        elif i == 7:
            fin[8] = comb[i][0]
	
    for i in {5, 6}:
        if i == 6:
            for n in comb[i]:
                if len(set(n).union(fin[7])) == 7:
                    fin[6] = n
                elif len(set(n).union(fin[4])) == 7:
                    fin[0] = n
                else:
                    fin[9] = n
        elif i == 5:
            for n in comb[i]:
                if len(set(n).union(fin[1])) == 5:
                    fin[3] = n
                elif len(set(n).union(fin[4])) == 7:
                    fin[2] = n
                else:
                    fin[5] = n

    c = ''
    for w in y:
        for i in range(10):
            if fin[i] == sorted(w):
                c += str(i)
                break
	
    count += int(c)

print(count)