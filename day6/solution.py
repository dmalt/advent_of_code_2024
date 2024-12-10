from copy import deepcopy

# input = "input_small.txt"
input = "input_large.txt"

with open(input) as f:
    labyrinth = list(map(lambda x: list(x.strip()), f))


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def find_guard(labyrinth: list[list[str]]) -> tuple[int, int, int, int]:
    for i, line in enumerate(labyrinth):
        for j, c in enumerate(line):
            if c in directions:
                labyrinth[i][j] = "."
                return (i, j) + directions[c]
    raise Exception


def turn(di, dj):
    return dj, -di


def make_move(labyrinth, i, j, di, dj) -> tuple[int, int, int, int]:
    next_i, next_j = i + di, j + dj
    assert next_i >= 0 and next_j >= 0
    c = labyrinth[next_i][next_j]
    if c == ".":
        return next_i, next_j, di, dj
    else:
        assert c == "#"
        di, dj = turn(di, dj)
        return i, j, di, dj


def track(labyrinth, i, j, di, dj):
    seen = {(i, j)}
    while True:
        try:
            i, j, di, dj = make_move(labyrinth, i, j, di, dj)
            if (i, j) not in seen:
                seen.add((i, j))
        except (IndexError, AssertionError):
            break
    return seen

def check_loop(ll, i, j, di, dj) -> bool:
    seen = {(i, j, di, dj)}
    while True:
        try:
            i, j, di, dj = make_move(ll, i, j, di, dj)
            if (i, j, di, dj) not in seen:
                seen.add((i, j, di, dj))
            else:
                return True
        except (IndexError, AssertionError):
            return False


i0, j0, di, dj = find_guard(labyrinth)
path = track(labyrinth, i0, j0, di, dj)
answer1 = len(path)

print(f"{answer1=}")

path.remove((i0, j0))

lala = []
answer2 = 0
for i_o, j_o in path:
    lab_ = deepcopy(labyrinth)
    lab_[i_o][j_o] = "#"

    if check_loop(lab_, i0, j0, di, dj):
        print(i_o, j_o)
        lala.append((i_o, j_o))
        answer2 += 1
print(f"{answer2=}") 
