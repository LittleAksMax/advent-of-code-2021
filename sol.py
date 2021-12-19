# data = [
#     [6,[[6,3],[[1,4],[8,4]]]],
#     [5,[[[0,8],[1,0]],8]],
#     [[[6,[7,7]],[2,[6,4]]],[2,6]],
#     [[[[7,4],[2,7]],[4,[1,5]]],[[[0,5],5],[[2,1],[8,2]]]],
#     [[[[5,9],[7,2]],[0,[9,9]]],[[[5,3],[7,9]],[3,[9,1]]]],
#     [5,[[3,0],[[8,2],5]]],
#     [[2,[[0,8],7]],[4,[7,7]]],
#     [[[[3,4],6],[5,[4,2]]],[[9,[9,5]],2]],
#     [[7,[0,5]],[[1,3],[7,[4,0]]]],
#     [[[6,2],3],[[[2,0],9],[5,[7,2]]]],
#     [[4,[8,6]],8],
#     [[[9,8],[[7,3],[4,6]]],[5,3]]
#     [[[0,[8,4]],8],[[5,[4,7]],[5,9]]]
#     [[[[0,8],[3,7]],[5,1]],[[5,6],2]]
#     [[[[5,8],0],[[3,0],3]],[[6,5],[[8,0],[3,9]]]]
#     [[[8,[5,6]],[6,4]],[8,0]]
#     [7,[[5,[3,8]],3]]
#     [[[4,[2,0]],2],[[[8,1],[5,8]],5]]
#     [9,[[[6,6],[8,1]],[[7,9],9]]]
#     [[[6,0],[[7,2],9]],[[[7,3],[1,1]],0]]
#     [[[[7,8],[0,3]],[5,9]],[[2,[4,3]],7]]
#     [[[3,1],[3,[6,3]]],[[6,[8,9]],7]]
#     [[[[1,1],[0,5]],[8,1]],[0,[8,[1,4]]]]
#     [[[6,[8,6]],[7,8]],[[7,3],[3,[5,8]]]]
#     [[[2,5],[[6,8],[4,5]]],[[2,[8,2]],[2,[3,2]]]]
#     [[[[9,2],0],5],0]
#     [[7,[[3,7],[0,9]]],[6,[1,[6,9]]]]
#     [[[[4,5],5],5],4]
#     [[[6,[6,9]],[8,3]],9]
#     [[[[2,7],[8,6]],0],[2,[4,9]]]
#     [[[4,[9,8]],[7,6]],[7,[[2,7],[2,7]]]]
#     [[[0,8],[4,[5,9]]],[[4,[1,0]],[6,8]]]
#     [[[2,4],9],[[[7,9],5],[0,5]]]
#     [[[3,[8,6]],6],[[8,[6,7]],[[6,1],[2,1]]]]
#     [[[0,[0,5]],[[0,5],4]],9]
#     [[[[0,0],7],8],[[8,[4,6]],9]]
#     [[[1,[1,1]],[3,[2,5]]],[6,6]]
#     [[[[3,7],[6,1]],[5,4]],[[0,[2,6]],[0,1]]]
#     [[1,1],[3,4]]
#     [9,[[4,[7,8]],[3,4]]]
#     [[[[5,3],[5,9]],9],[[[2,4],[2,7]],[[6,3],[1,8]]]]
#     [[[2,[2,2]],[[8,7],9]],[[[4,6],[5,3]],[[2,6],9]]]
#     [[[3,8],[[5,7],7]],[[[0,9],3],1]]
#     [[[6,[1,9]],[2,1]],[[[7,0],[2,1]],8]]
#     [[[8,[9,9]],1],[[4,1],[[2,8],1]]]
#     [[[2,[3,7]],[[2,4],[3,5]]],[[3,[1,9]],[[1,3],[1,7]]]]
#     [[[[4,3],8],3],[[6,[1,7]],[[4,2],9]]]
#     [[[[1,9],1],[[0,7],[9,4]]],[[[7,2],[0,1]],8]]
#     [9,5]
#     [[[[6,4],4],[[3,4],0]],[[9,[7,6]],[[3,4],[7,1]]]]
#     [[0,2],[[[4,9],[3,4]],[2,[3,9]]]]
#     [[[[8,9],9],[[6,4],[2,9]]],[[4,5],[[1,8],2]]]
#     [[[6,[9,5]],[4,[1,0]]],[[[4,1],[3,5]],[3,3]]]
#     [[[7,1],[[5,4],8]],[[0,[9,4]],7]]
#     [[[4,[0,3]],[[0,2],8]],[[0,[9,6]],[[6,3],[3,2]]]]
#     [[[[5,5],8],[[4,5],3]],[3,[[0,2],0]]]
#     [[[[9,5],[1,0]],[[9,1],[0,9]]],[[1,[9,1]],[1,3]]]
#     [[9,[[5,7],8]],[[9,[9,3]],[3,[0,1]]]]
#     [[[5,6],[9,8]],[2,9]]
#     [[[9,[3,8]],[9,0]],[[8,[6,2]],1]]
#     [3,[4,[1,[0,4]]]]
#     [[9,[[8,5],[8,0]]],[[1,6],[8,4]]]
#     [[7,[[6,8],5]],[[9,[1,3]],[[6,5],[0,8]]]]
#     [[[6,0],[9,[3,5]]],[8,6]]
#     [[[1,[2,3]],[[5,2],4]],[1,[[7,3],2]]]
#     [[[2,[1,1]],3],[[8,[5,5]],[[7,5],[8,9]]]]
#     [[[4,0],[8,6]],[[[7,1],7],0]]
#     [2,6]
#     [[[[5,4],[9,7]],4],[0,6]]
#     [[4,[0,5]],[1,[[1,6],[6,2]]]]
#     [[[7,8],[0,6]],[0,[[2,9],[1,5]]]]
#     [1,[[[4,4],1],[[3,2],[2,5]]]]
#     [[[[9,8],[2,4]],[1,2]],[[[5,1],9],[[0,8],[5,2]]]]
#     [[8,[[2,6],[4,6]]],[[0,[2,9]],[[2,2],[7,2]]]]
#     [[[7,[8,1]],[[8,8],7]],[3,[7,[7,9]]]]
#     [[6,[[3,1],[3,6]]],[[[5,8],[9,8]],[2,[7,4]]]]
#     [[[4,[2,0]],[3,[3,3]]],[[6,[8,5]],5]]
#     [[[3,2],3],[[8,2],8]]
#     [[7,[[8,7],[5,8]]],[[2,0],[7,7]]]
#     [[[[3,3],1],[[5,1],4]],[[4,3],[[4,9],8]]]
#     [[[0,[5,8]],7],[4,9]]
#     [[0,[[7,7],[1,1]]],[[0,[5,0]],[4,5]]]
#     [[[[2,8],[1,6]],[[7,3],9]],[[2,8],[6,2]]]
#     [[1,[4,7]],[8,0]]
#     [3,[[[6,1],9],[[1,1],5]]]
#     [[[[3,0],[9,8]],[6,[8,3]]],3]
#     [4,[[1,[8,1]],[[6,0],2]]]
#     [[4,[4,[0,3]]],[[[7,5],[0,2]],[[9,7],[6,5]]]]
#     [[0,[4,[6,1]]],[[[1,9],[6,0]],9]]
#     [[[[0,2],[8,4]],[2,3]],[[9,[8,4]],1]]
#     [[[[1,2],[7,7]],[[3,8],3]],[[[1,1],[7,5]],6]]
#     [[[[1,8],[8,4]],[[4,0],1]],[0,[1,[9,4]]]]
#     [[[3,1],[9,5]],[[[9,5],4],[[8,7],4]]]
#     [[[6,[3,0]],0],[[[6,9],7],[[6,1],[6,6]]]]
#     [[[[9,6],[4,4]],5],9]
#     [[5,[[6,0],0]],1]
#     [3,[0,[4,[9,0]]]]
#     [[[5,[2,2]],3],5]
#     [[2,3],[9,[6,7]]]
#     [[[[6,8],[7,9]],[4,7]],[[1,2],[0,1]]]
# ]

def reduce_snailfish(full_pair_str, debug=False):
    new_full_pair_str = full_pair_str
    nest_lvl = 0
    explode_left = explode_right = None
    last_seen_value = None
    operated = False
    if debug:
        print(new_full_pair_str)
    for i, ch in enumerate(new_full_pair_str):
        if ch == "[":
            nest_lvl += 1
            if nest_lvl >= 5:
                j = new_full_pair_str.index("]", i)
                explode_left, explode_right = explode(new_full_pair_str, i, j)
                new_full_pair_str = f"{new_full_pair_str[:i]}0{new_full_pair_str[j+1:]}"
                next_value, next_indices = get_next_value(new_full_pair_str, i + 1)
                last_value, last_indices = get_last_value(new_full_pair_str, i - 1)
                if next_value is not None:
                    new_full_pair_str = replace_value(
                        new_full_pair_str, next_indices, next_value + explode_right
                    )
                if last_value is not None:
                    new_full_pair_str = replace_value(
                        new_full_pair_str, last_indices, last_value + explode_left
                    )
                nest_lvl -= 1
                operated = True
                if debug:
                    print(f"EXPLODED [{explode_left},{explode_right}]!")
                break
        if ch == "]":
            nest_lvl -= 1
        if ch == ",":
            continue
    if not operated:
        for i, ch in enumerate(new_full_pair_str):
            if next_value_index := get_next_value(new_full_pair_str, i):
                value, indices = next_value_index
                if value is not None and value >= 10:
                    # split
                    new_pair = f"[{value//2},{value//2+value%2}]"
                    new_full_pair_str = replace_value(
                        new_full_pair_str, indices, new_pair
                    )
                    operated = True
                    if debug:
                        print(f"SPLIT {value}!")
                    break
    if operated:
        return reduce_snailfish(new_full_pair_str, debug=debug)
    return new_full_pair_str


def explode(full_pair_str, pair_start, pair_end):
    return map(int, full_pair_str[pair_start + 1 : pair_end].split(",", maxsplit=1))


def get_next_value(full_pair_str, idx):
    # Get first numeric value starting at idx, returns it and its start and end indices
    # If none exists, returns None, None
    remaining_str = full_pair_str[idx:]
    value = ""
    for j, ch in enumerate(remaining_str):
        if ch.isdigit():
            k = j
            while remaining_str[k].isdigit():
                value += remaining_str[k]
                k += 1
            return int(value), (idx + j, idx + k)
    return None, None


def get_last_value(full_pair_str, idx):
    # Get last numeric value up to index idx, returns it and its index and its end index
    # If none exists, returns None, None
    value = ""
    for j in range(idx, -1, -1):
        ch = full_pair_str[j]
        if ch.isdigit():
            k = j
            while full_pair_str[k].isdigit():
                value = full_pair_str[k] + value
                k -= 1
            return (
                int(value),
                (k + 1, j + 1),
            )
    return None, None


def replace_value(full_pair_str, idx, new_value):
    # Remove numeric value starting at idx, replaces it with new_value
    new_str = f"{full_pair_str[: idx[0]]}{new_value}{full_pair_str[idx[1] :]}"
    return new_str


def calc_magnitude(value):
    if isinstance(value, int):
        return value
    return 3 * calc_magnitude(value[0]) + 2 * calc_magnitude(value[1])


input_data = open("input.txt", "r").read().strip().split("\n")

# Part 1:
reduced = input_data[0]
for row in input_data[1:]:
    pair_sum = f"[{reduced},{row}]"
    reduced = reduce_snailfish(pair_sum, debug=False)
print(calc_magnitude(eval(reduced)))

# Part 2:
reduced_rows = [
    reduce_snailfish(f"[{row_i},{row_j}]", debug=False)
    for row_i in input_data
    for row_j in input_data
    if row_i != row_j
]
magnitudes = [calc_magnitude(eval(reduced)) for reduced in reduced_rows]
print(max(magnitudes))