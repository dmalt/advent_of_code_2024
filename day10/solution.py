def get(arr, i, j) -> tuple[int, int, int]:
    if not (0 <= i < len(arr)):
        return -1, i, j
    if not (0 <= j < len(arr[0])):
        return -1, i, j

    return arr[i][j], i, j


def get_neigh(
    arr: list[list[int]], i: int, j: int, target: int
) -> list[tuple[int, int, int]]:
    candidates = [
        get(arr, i - 1, j),
        get(arr, i + 1, j),
        get(arr, i, j - 1),
        get(arr, i, j + 1),
    ]
    return [(c, i, j) for c, i, j in candidates if c == target]


def find_headstarts(arr):
    res = []
    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c == 0:
                res.append((i, j))
    return res


def compute_score(arr: list[list[int]], i: int, j: int):
    stack = []
    target = 1
    stack.extend(get_neigh(arr, i, j, target))
    score = 0
    seen = set()

    while stack:
        # print(f"{stack=}") 
        c, i, j = stack.pop()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        if c == 9:
            # print(f"done: {i=}, {j=}") 
            score += 1
        else:
            stack.extend(get_neigh(arr, i, j, c + 1))
    return score

def compute_rating(arr: list[list[int]], i: int, j: int):
    stack = []
    target = 1
    stack.extend(get_neigh(arr, i, j, target))
    score = 0
    # seen = set()

    while stack:
        # print(f"{stack=}") 
        c, i, j = stack.pop()
        # if (i, j) in seen:
        #     continue
        # seen.add((i, j))
        if c == 9:
            # print(f"done: {i=}, {j=}") 
            score += 1
        else:
            stack.extend(get_neigh(arr, i, j, c + 1))
    return score

def print_arr(arr):
    for line in arr:
        print("".join(map(str, line)))


arr = []
with open("input_large.txt") as f:
    for line in f:
        arr.append(list(map(int, line.strip())))

print_arr(arr)
headstarts = find_headstarts(arr)
print(headstarts)

answer1 = 0
answer2 = 0
for i0, j0 in headstarts:
    score = compute_score(arr, i0, j0)
    rating = compute_rating(arr, i0, j0)
    answer1 += score
    answer2 += rating
    # print(f"{score=}")

print(f"{answer1=}") 
print(f"{answer2=}") 
