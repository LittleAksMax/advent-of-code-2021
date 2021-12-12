
# data = None
# with open("input.txt", "r") as f:
#     data = [line for line in f.read().splitlines()]

# graph = {}
# for line in data:
#     x, y = line.split("-")
#     if x not in graph.keys():
#         graph[x] = []
#     if y not in graph.keys():
#         graph[y] = []
#     graph[x].append(y)
#     graph[y].append(x)

# def find_paths_A(graph, start, visited):

#     cur = start
#     if cur == "start": visited.append(cur)
#     if cur == "end":
#         return 1
#     opts = [pos for pos in graph[cur] if pos not in visited]
#     visited_ = visited.copy()
#     if cur.islower():
#         visited_.append(cur)
#     count = 0
#     for opt in opts:
#         count += find_paths_A(graph, opt, visited_)
#     return count

# def find_paths_B(graph, pos, visited, fullvisited):
#     if pos == "end":
#         fullvisited_ = fullvisited.copy()
#         fullvisited_.append(pos)
#         # Uncomment if you want all full paths printed:
#         # print(newfullvisited)
#         return 1
#     else:
#         if "secondtime" not in visited and pos not in visited:
#             options = [i for i in graph[pos] if i != "start"]
#         else:
#             options = [i for i in graph[pos] if i not in visited and i != "start"] 
#         visited_ = visited.copy()
#         fullvisited_ = fullvisited.copy()
#         if pos in visited:
#             visited_.append("secondtime")
#         if pos.islower() and pos != "start":
#             visited_.append(pos)

#         fullvisited_.append(pos)


#         count = 0
#         for option in options:
#             count += find_paths_B(graph, option, visited_, fullvisited_)

#         return count

# print(find_paths_B(graph, "start", [], []))

import networkx as nx

# NOTE: I STOLE THIS CODE FOR PART B, I DON'T KNOW WHY THE ABOVE DIDN'T WORK

def visit(node='start', visited=set(), double=False):
    if node == 'end':
        return 1
    if node in visited:
        if double:
            return 0
        else:
            if node == 'start':
                return 0
            double = True
    v = visited.copy()
    if node.islower():
        v.add(node)
    sum = 0
    for child in caves[node]:
        sum += visit(child, v, double)
    return sum

with open('input.txt', "r") as f:
    caves = nx.Graph([tuple(l.strip().split('-')) for l in f.readlines()])

print(visit())

